<script>
  import MainTopBar from '../components/MainTopBar.svelte';

  /**
   * onBack      — navigate back to home
   * onStart     — called with the selected module to start a new game
   */
  let { onBack, onStart } = $props();

  // ── Available adventure modules ───────────────────────────────────────────────
  const MODULES = [
    {
      id: 'ravenloft',
      title: "La Piaga di Ravenloft",
      setting: "Horror Gotico",
      difficulty: 'Difficile',
      diffClass: 'hard',
      players: '1 giocatore',
      description: "Un antico male risvegliato scorre tra le nebbie di Barovia. Sopravvivi alle cripte di Strahd e svela la maledizione che tormenta questa terra.",
      tags: ['Orrore', 'Vampiri', 'Nebbia'],
    },
    {
      id: 'phandelver',
      title: "Miniere di Phandelver",
      setting: "Alta Fantasia",
      difficulty: 'Normale',
      diffClass: 'normal',
      players: '1 giocatore',
      description: "La Grotta dell'Onda Tonante custodisce antichi segreti. Esplora le terre selvagge attorno a Phandalin e affronta il misterioso Ragno Nero.",
      tags: ['Esplorazione', 'Goblin', 'Magia'],
    },
    {
      id: 'undermountain',
      title: "Profondità di Undermountain",
      setting: "Dungeon Crawler",
      difficulty: 'Leggendario',
      diffClass: 'legendary',
      players: '1 giocatore',
      description: "Il mega-dungeon sotto Waterdeep è infinito. Ogni livello cela orrori più grandi. Solo i più audaci sopravvivono ai labirinti di Halaster.",
      tags: ['Dungeon', 'Puzzle', 'Mostri'],
    },
    {
      id: 'icewind',
      title: "Icewind Dale — Confine del Ghiaccio",
      setting: "Avventura Artica",
      difficulty: 'Normale',
      diffClass: 'normal',
      players: '1 giocatore',
      description: "Una notte eterna cala su Icewind Dale. Le Dieci Città sopravvivono a stento mentre creature del freddo stringono d'assedio le mura.",
      tags: ['Ghiaccio', 'Sopravvivenza', 'Mito'],
    },
  ];

  let selectedId = $state(null);

  function handleSelect(id) {
    selectedId = selectedId === id ? null : id;
  }

  function handleStart() {
    const module = MODULES.find(m => m.id === selectedId);
    if (module) onStart?.(module);
  }
</script>

<div class="new-campaign">
  <MainTopBar />

  <div class="page-content">
    <!-- Back link -->
    <button class="back-link" onclick={onBack}>
      <svg class="back-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
      </svg>
      Indietro al Menù Principale
    </button>

    <!-- Page header -->
    <div class="page-header">
      <h1 class="page-title">Nuova Campagna</h1>
      <p class="page-subtitle">Scegli il modulo d&apos;avventura e lascia che il Master IA scriva il tuo destino.</p>
    </div>

    <!-- Module grid -->
    <div class="module-grid" role="list">
      {#each MODULES as mod (mod.id)}
        <button
          class="module-card"
          class:selected={selectedId === mod.id}
          onclick={() => handleSelect(mod.id)}
          role="listitem"
          aria-pressed={selectedId === mod.id}
        >
          <!-- Left accent stripe (difficulty color) -->
          <span class="diff-stripe {mod.diffClass}" aria-hidden="true"></span>

          <!-- Thumbnail placeholder -->
          <div class="mod-thumb" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 3H7v2H5V3H3v6h2v11h14V9h2V3h-2v2h-2V3h-2v2h-2V3H9zm7 16H8V9h8v10z" />
            </svg>
          </div>

          <!-- Info -->
          <div class="mod-info">
            <div class="mod-meta">
              <span class="mod-setting">{mod.setting}</span>
              <span class="mod-players">{mod.players}</span>
            </div>
            <h3 class="mod-title">{mod.title}</h3>
            <p class="mod-desc">{mod.description}</p>
            <div class="mod-tags">
              {#each mod.tags as tag}
                <span class="tag">{tag}</span>
              {/each}
            </div>
          </div>

          <!-- Difficulty badge -->
          <div class="mod-right">
            <span class="diff-badge {mod.diffClass}">{mod.difficulty}</span>
            {#if selectedId === mod.id}
              <div class="check-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" />
                </svg>
              </div>
            {/if}
          </div>
        </button>
      {/each}
    </div>
  </div>

  <!-- Sticky CTA -->
  <div class="cta-bar" class:visible={selectedId !== null}>
    <p class="cta-hint">
      {#if selectedId}
        {@const mod = MODULES.find(m => m.id === selectedId)}
        Hai selezionato: <strong>{mod?.title}</strong>
      {/if}
    </p>
    <button class="btn-start" onclick={handleStart} disabled={!selectedId}>
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M8 5v14l11-7z" />
      </svg>
      INIZIA AVVENTURA
    </button>
  </div>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  // ── Page shell ───────────────────────────────────────────────────────────────
  .new-campaign {
    min-height: 100vh;
    background: $color-bg-page;
    color: $color-text-primary;
    display: flex;
    flex-direction: column;
    padding-bottom: 90px;
  }

  .page-content {
    flex: 1;
    max-width: $campaign-max-width;
    width: 100%;
    margin: 0 auto;
    padding: $space-10 $space-9 $space-6;
  }

  // ── Back link ─────────────────────────────────────────────────────────────────
  .back-link {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-accent;
    padding: 0;
    margin-bottom: $space-9;
    transition: opacity $transition-base;

    &:hover { opacity: 0.75; }
  }

  .back-icon {
    width: 18px;
    height: 18px;
  }

  // ── Page header ───────────────────────────────────────────────────────────────
  .page-header {
    margin-bottom: $space-9;
  }

  .page-title {
    font-family: $font-sans;
    font-size: clamp(28px, 4vw, 40px);
    font-weight: $font-weight-black;
    color: $white;
    margin: 0 0 $space-3;
  }

  .page-subtitle {
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-primary;
    margin: 0;
    line-height: 1.5;
  }

  // ── Module grid ───────────────────────────────────────────────────────────────
  .module-grid {
    display: flex;
    flex-direction: column;
    gap: $space-4;
  }

  .module-card {
    position: relative;
    display: flex;
    align-items: flex-start;
    gap: $space-6;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-lg;
    padding: $space-6 $space-7 $space-6 calc($space-7 + 6px);
    text-align: left;
    cursor: pointer;
    transition: border-color $transition-base, background $transition-base, box-shadow $transition-base;
    overflow: hidden;

    &:hover {
      border-color: $color-border;
      background: $color-surface-elevated;
    }

    &.selected {
      border-color: $color-accent;
      box-shadow: 0 0 0 1px rgba($gold-500, 0.25) inset;
    }
  }

  // ── Left difficulty stripe ────────────────────────────────────────────────────
  .diff-stripe {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    border-radius: $radius-lg 0 0 $radius-lg;

    &.normal     { background: $hp-full; }
    &.hard       { background: $hp-mid; }
    &.legendary  { background: $red-400; }
  }

  // ── Thumbnail ────────────────────────────────────────────────────────────────
  .mod-thumb {
    flex-shrink: 0;
    width: 56px;
    height: 56px;
    border-radius: $radius-md;
    background: $color-bg-page;
    border: 1px solid $color-border-subtle;
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgba($gold-500, 0.20);
    margin-top: 2px;

    svg {
      width: 28px;
      height: 28px;
    }
  }

  // ── Module info ───────────────────────────────────────────────────────────────
  .mod-info {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: $space-1 + 2px;
  }

  .mod-meta {
    display: flex;
    gap: $space-3;
    font-family: $font-sans;
    font-size: $font-size-caption;
    color: $color-text-secondary;
  }

  .mod-setting {
    color: $color-accent;
    font-weight: $font-weight-semibold;
  }

  .mod-title {
    font-family: $font-sans;
    font-size: $campaign-title-size;
    font-weight: $font-weight-black;
    color: $white;
    margin: 0;
    line-height: 1.2;
  }

  .mod-desc {
    font-family: $font-sans;
    font-size: $font-size-caption;
    color: $color-text-primary;
    margin: 0;
    line-height: 1.5;
  }

  .mod-tags {
    display: flex;
    flex-wrap: wrap;
    gap: $space-1 + 2px;
    margin-top: $space-1;
  }

  .tag {
    font-family: $font-sans;
    font-size: 11px;
    font-weight: $font-weight-semibold;
    color: $color-accent;
    background: rgba($gold-500, 0.10);
    border: 1px solid rgba($gold-500, 0.20);
    border-radius: 999px;
    padding: 2px $space-3;
    letter-spacing: 0.5px;
  }

  // ── Right: badge + check ──────────────────────────────────────────────────────
  .mod-right {
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: $space-3;
    padding-top: 2px;
  }

  .diff-badge {
    font-family: $font-sans;
    font-size: 11px;
    font-weight: $font-weight-bold;
    letter-spacing: 0.5px;
    border-radius: 999px;
    padding: 3px $space-4;
    white-space: nowrap;

    &.normal    { background: rgba($hp-full, 0.15); color: $hp-full; }
    &.hard      { background: rgba($hp-mid,  0.15); color: $hp-mid;  }
    &.legendary { background: rgba($red-400, 0.15); color: $red-400; }
  }

  .check-icon {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: $color-accent;
    color: $dark-700;
    display: flex;
    align-items: center;
    justify-content: center;

    svg {
      width: 14px;
      height: 14px;
    }
  }

  // ── Sticky CTA bar ────────────────────────────────────────────────────────────
  .cta-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: $color-surface;
    border-top: 1px solid $color-border-subtle;
    padding: $space-5 $space-9;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: $space-6;
    z-index: $z-bottombar;
    transform: translateY(100%);
    transition: transform $transition-base;

    &.visible {
      transform: translateY(0);
    }
  }

  .cta-hint {
    font-family: $font-sans;
    font-size: $font-size-caption;
    color: $color-text-secondary;
    margin: 0;

    strong {
      color: $white;
      font-weight: $font-weight-bold;
    }
  }

  .btn-start {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    padding: $space-4 $space-10;
    background: $color-btn-primary-bg;
    border: none;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-serif;
    font-size: $font-size-btn;
    font-weight: $font-weight-black;
    letter-spacing: $letter-spacing-btn;
    color: $color-btn-primary-text;
    white-space: nowrap;
    transition: $transition-btn;

    svg {
      width: 18px;
      height: 18px;
    }

    &:hover:not(:disabled) {
      background: $color-btn-primary-hover-bg;
      box-shadow: $glow-btn-primary;
      transform: translateY(-1px);
    }

    &:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }
  }
</style>
