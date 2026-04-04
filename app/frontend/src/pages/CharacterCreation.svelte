<script lang="ts">
  import AppTopBar from '../components/AppTopBar.svelte';
  import FormField from '../components/FormField.svelte';
  import SelectField from '../components/SelectField.svelte';
  import AspectPanel from '../components/AspectPanel.svelte';
  import AttributeCard from '../components/AttributeCard.svelte';
  import type { AttrKey, AttrMap, AttrMode } from '../lib/types.js';

  interface Props {
    onBack?: () => void;
  }

  let { onBack = () => {} }: Props = $props();

  // ── Form state ───────────────────────────────────────────────────────────────
  let name       = $state<string>('');
  let race       = $state<string>('Umano');
  let charClass  = $state<string>('Guerriero');
  let background = $state<string>('Soldato');

  // ── Attribute generation mode ────────────────────────────────────────────────
  let mode = $state<AttrMode>('standard');

  // ── Point-buy state ──────────────────────────────────────────────────────────
  const POINT_TOTAL = 27;
  const COST: Record<number, number> = { 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9 };

  let attrs = $state<AttrMap>({
    forza:        10,
    destrezza:    12,
    costituzione: 10,
    intelligenza:  8,
    saggezza:     10,
    carisma:      14,
  });

  let spentPoints = $derived(
    Object.values(attrs).reduce((sum: number, v: number) => sum + (COST[v] ?? 0), 0)
  );
  let remainingPoints = $derived(POINT_TOTAL - spentPoints);

  function increment(attr: AttrKey): void {
    const next = attrs[attr] + 1;
    if (next <= 15 && (COST[next] ?? 0) - (COST[attrs[attr]] ?? 0) <= remainingPoints) {
      attrs[attr] = next;
    }
  }

  function decrement(attr: AttrKey): void {
    if (attrs[attr] > 8) attrs[attr]--;
  }

  function canIncrement(attr: AttrKey): boolean {
    if (mode === 'random') return false;
    const next = attrs[attr] + 1;
    return next <= 15 && (COST[next] ?? 0) - (COST[attrs[attr]] ?? 0) <= remainingPoints;
  }

  function canDecrement(attr: AttrKey): boolean {
    if (mode === 'random') return false;
    return attrs[attr] > 8;
  }

  function rollRandom(): void {
    const attrKeys = Object.keys(attrs) as AttrKey[];
    attrKeys.forEach((key) => {
      // Roll 4d6 drop lowest
      const rolls = Array.from({ length: 4 }, () => Math.ceil(Math.random() * 6));
      rolls.sort((a, b) => a - b);
      attrs[key] = rolls.slice(1).reduce((s, v) => s + v, 0);
    });
  }

  function handleModeChange(newMode: AttrMode): void {
    mode = newMode;
    if (newMode === 'random') rollRandom();
    else {
      attrs = { forza: 10, destrezza: 12, costituzione: 10, intelligenza: 8, saggezza: 10, carisma: 14 };
    }
  }

  // ── Select options ───────────────────────────────────────────────────────────
  const races: string[]       = ['Umano', 'Elfo', 'Nano', 'Halfling', 'Gnomo', 'Mezzelfo', 'Mezzorco', 'Tiefling', 'Draconico'];
  const classes: string[]     = ['Barbaro', 'Bardo', 'Chierico', 'Druido', 'Guerriero', 'Monaco', 'Paladino', 'Ranger', 'Ladro', 'Stregone', 'Warlock', 'Mago'];
  const backgrounds: string[] = ['Accolito', 'Criminale', 'Eremita', 'Eroe Popolare', 'Gildista', 'Nobile', 'Orfano', 'Saggio', 'Soldato', 'Vagabondo'];

  // ── Attribute display order ──────────────────────────────────────────────────
  const attrMeta: { key: AttrKey; label: string }[] = [
    { key: 'forza',        label: 'FORZA' },
    { key: 'destrezza',    label: 'DESTREZZA' },
    { key: 'costituzione', label: 'COSTITUZIONE' },
    { key: 'intelligenza', label: 'INTELLIGENZA' },
    { key: 'saggezza',     label: 'SAGGEZZA' },
    { key: 'carisma',      label: 'CARISMA' },
  ];
</script>

<div class="char-creation">
  <AppTopBar {onBack} />

  <!-- Scrollable content -->
  <div class="char-content">

    <!-- ── Page header ──────────────────────────────────────────────────────── -->
    <div class="page-header">
      <h1 class="page-title">Creazione Personaggio</h1>
      <p class="page-subtitle">Plasma il tuo destino nelle tenebre del dungeon.</p>
    </div>

    <!-- ── Two-column section ───────────────────────────────────────────────── -->
    <div class="two-col">

      <!-- Left column -->
      <div class="col-left">
        <section class="form-section">
          <h2 class="section-title">Nome del Personaggio</h2>
          <FormField placeholder="Come verrai ricordato?" bind:value={name} />
        </section>

        <section class="form-section">
          <h2 class="section-title">Origini e Vocazione</h2>
          <div class="selects-stack">
            <SelectField label="RAZZA" options={races} bind:value={race} />
            <SelectField label="CLASSE" options={classes} bind:value={charClass} />
            <SelectField label="BACKGROUND" options={backgrounds} bind:value={background} />
          </div>
        </section>
      </div>

      <!-- Right column -->
      <div class="col-right">
        <h2 class="section-title">Aspetto Visivo</h2>
        <AspectPanel />
      </div>
    </div>

    <!-- ── Attributi section ──────────────────────────────────────────────── -->
    <section class="attr-section">
      <div class="attr-section-header">
        <h2 class="section-title">Attributi</h2>

        <div class="attr-section-controls">
          <div class="mode-toggle" role="group" aria-label="Modalità generazione attributi">
            <button
              class="mode-btn"
              class:active={mode === 'standard'}
              onclick={() => handleModeChange('standard')}
            >
              SERIE STANDARD
            </button>
            <button
              class="mode-btn"
              class:active={mode === 'random'}
              onclick={() => handleModeChange('random')}
            >
              GENERAZIONE CASUALE
            </button>
          </div>

          {#if mode === 'standard'}
            <span class="points-remaining">Punti Rimanenti: {remainingPoints}</span>
          {/if}
        </div>
      </div>

      <div class="attr-grid">
        {#each attrMeta as { key, label }}
          <AttributeCard
            {label}
            value={attrs[key]}
            canIncrement={canIncrement(key)}
            canDecrement={canDecrement(key)}
            onIncrement={() => increment(key)}
            onDecrement={() => decrement(key)}
          />
        {/each}
      </div>
    </section>

  </div><!-- /char-content -->

  <!-- ── Sticky bottom bar ──────────────────────────────────────────────────── -->
  <div class="bottom-bar">
    <div class="bottom-divider" aria-hidden="true"></div>
    <button class="btn-create">
      CREA PERSONAGGIO
      <svg class="swords-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M6.92 5H5L3 7l1.41 1.41L6 6.83l1 1-4.29 4.3 1.41 1.41L8.83 8.83l2.85 2.85-1.42 1.41 1.42 1.42 1.41-1.42 1.42 1.42 1.41-1.41-1.42-1.42 4.25-4.24-1.41-1.42L13.17 9.17l-1-1 1.59-1.58L15.17 8l1.41-1.41L15 5h-1.92L9 9.08 6.92 5zM20 17l-4-4-1.06 1.06 4 4L20 17zm-9.17.17l-.71.7L9 16.76l.71-.71-1.42-1.41-.7.7-1.42-1.41.7-.71-1.41-1.41-2.83 2.83 5.66 5.66 2.83-2.83-1.42-1.41z" />
      </svg>
    </button>
    <p class="bottom-disclaimer">
      Premendo il tasto, il tuo viaggio nel Dungeon avrà inizio. Non c'è ritorno.
    </p>
  </div>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  // ── Page shell ───────────────────────────────────────────────────────────────
  .char-creation {
    min-height: 100vh;
    background-color: $color-bg-page;
    color: $color-text-primary;
    display: flex;
    flex-direction: column;
  }

  // ── Scrollable content ───────────────────────────────────────────────────────
  .char-content {
    flex: 1;
    max-width: 1100px;
    width: 100%;
    margin: 0 auto;
    padding: calc(#{$topbar-height} + 40px) $space-9 160px;
  }

  // ── Page header ──────────────────────────────────────────────────────────────
  .page-header {
    margin-bottom: $space-13;
  }

  .page-title {
    font-family: $font-sans;
    font-size: $font-size-page-title;
    font-weight: $font-weight-black;
    color: $color-text-primary;
    line-height: 1.1;
    margin: 0 0 $space-3;
  }

  .page-subtitle {
    font-family: $font-sans;
    font-size: $font-size-body;
    font-style: italic;
    color: $color-text-muted;
    margin: 0;
  }

  // ── Section title (shared) ───────────────────────────────────────────────────
  .section-title {
    font-family: $font-sans;
    font-size: $font-size-section-label;
    font-weight: $font-weight-bold;
    color: $color-text-primary;
    margin: 0 0 $space-5;
  }

  // ── Two-column layout ────────────────────────────────────────────────────────
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: $space-9;
    margin-bottom: $space-13;

    @media (max-width: 768px) {
      grid-template-columns: 1fr;
    }
  }

  // ── Left column ──────────────────────────────────────────────────────────────
  .col-left {
    display: flex;
    flex-direction: column;
    gap: $space-9;
  }

  .form-section {
    display: flex;
    flex-direction: column;
  }

  .selects-stack {
    display: flex;
    flex-direction: column;
    gap: $space-3;
  }

  // ── Right column ─────────────────────────────────────────────────────────────
  .col-right {
    display: flex;
    flex-direction: column;
  }

  // ── Attributi section ────────────────────────────────────────────────────────
  .attr-section {
    display: flex;
    flex-direction: column;
    gap: $space-6;
  }

  .attr-section-header {
    display: flex;
    align-items: center;
    gap: $space-6;
    flex-wrap: wrap;

    .section-title {
      margin: 0;
      flex-shrink: 0;
    }
  }

  .attr-section-controls {
    display: flex;
    align-items: center;
    gap: $space-5;
    flex-wrap: wrap;
    margin-left: auto;
  }

  // ── Mode toggle ──────────────────────────────────────────────────────────────
  .mode-toggle {
    display: flex;
    border-radius: $radius-sm;
    overflow: hidden;
    border: 1px solid $color-border;
  }

  .mode-btn {
    padding: $space-2 $space-5;
    background: $color-surface;
    border: none;
    cursor: pointer;
    font-family: $font-serif;
    font-size: $font-size-field-label;
    font-weight: $font-weight-bold;
    letter-spacing: $letter-spacing-label;
    text-transform: uppercase;
    color: $color-text-secondary;
    transition: background $transition-fast, color $transition-fast;

    & + & {
      border-left: 1px solid $color-border;
    }

    &.active {
      background: $color-surface-elevated;
      color: $color-accent;
    }

    &:hover:not(.active) {
      background: $color-surface-elevated;
      color: $color-text-primary;
    }
  }

  .points-remaining {
    font-family: $font-serif;
    font-size: $font-size-caption;
    font-weight: $font-weight-bold;
    letter-spacing: $letter-spacing-label;
    color: $color-accent;
    white-space: nowrap;
  }

  // ── Attribute grid (3 columns) ────────────────────────────────────────────────
  .attr-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: $space-4;

    @media (max-width: 640px) {
      grid-template-columns: repeat(2, 1fr);
    }

    @media (max-width: 400px) {
      grid-template-columns: 1fr;
    }
  }

  // ── Sticky bottom bar ─────────────────────────────────────────────────────────
  .bottom-bar {
    position: sticky;
    bottom: 0;
    background: $color-bg-page;
    padding: 0 $space-9 $space-9;
    z-index: $z-bottombar;
  }

  .bottom-divider {
    height: 1px;
    background: $color-border-subtle;
    margin-bottom: $space-7;
  }

  .btn-create {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: $space-4;
    width: 100%;
    max-width: 1100px;
    margin: 0 auto $space-4;
    padding: 20px $space-9;
    background: $color-btn-primary-bg;
    border: none;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-serif;
    font-size: $font-size-btn;
    font-weight: $font-weight-black;
    letter-spacing: $letter-spacing-btn;
    color: $color-btn-primary-text;
    transition: $transition-btn;

    &:hover {
      background: $color-btn-primary-hover-bg;
      box-shadow: $glow-btn-primary;
      transform: translateY(-1px);
    }

    &:active {
      transform: translateY(1px);
    }
  }

  .swords-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
  }

  .bottom-disclaimer {
    font-family: $font-sans;
    font-size: $font-size-caption;
    color: $color-text-secondary;
    text-align: center;
    margin: 0;
  }
</style>
