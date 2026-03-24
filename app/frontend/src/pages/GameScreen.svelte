<script>
  /**
   * campaign   — the active campaign object (id, title, charName, charClass, charLevel)
   * onBack     — navigate back (to home / LoadCampaign)
   * onBattle   — navigate to BattleView
   */
  let { campaign = {}, onBack, onBattle } = $props();

  // ── Demo game state ───────────────────────────────────────────────────────────
  let charHp    = $state(62);
  const charMaxHp = 80;
  let charMp    = $state(24);
  const charMaxMp = 30;

  let narrative = $state(
    "Le fiamme delle torce proiettano ombre danzanti sulle mura di pietra. L'aria sa di muffa e di sangue antico. Davanti a te, un corridoio si snoda verso le profondità del dungeon.\n\nUn tenue lamento echeggia da qualche parte nell'oscurità — troppo umano per essere ignorato."
  );

  let inputText = $state('');

  const QUICK_ACTIONS = [
    { id: 'explore',   label: 'Esplora',   icon: 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z' },
    { id: 'talk',      label: 'Parla',     icon: 'M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z' },
    { id: 'combat',    label: 'Combatti',  icon: 'M7.5 5.6L10 7 8.6 4.5 10 2 7.5 3.4 5 2l1.4 2.5L5 7zm12 9.8L17 14l1.4 2.5L17 19l2.5-1.4L22 19l-1.4-2.5L22 14zM22 2l-2.5 1.4L17 2l1.4 2.5L17 7l2.5-1.4L22 7l-1.4-2.5zm-7.63 5.29a1.5 1.5 0 00-2.12 0L3 16.54V21h4.46l9.25-9.25a1.5 1.5 0 000-2.12l-2.34-2.34z' },
    { id: 'inventory', label: 'Inventario',icon: 'M20 6h-2.18c.07-.44.18-.88.18-1.36C18 2.51 15.49 0 12 0 8.51 0 6 2.51 6 4.64c0 .48.11.92.18 1.36H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-8-4c1.84 0 3 1.16 3 2.64 0 .49-.27.92-.55 1.36h-4.9C9.27 5.56 9 5.13 9 4.64 9 3.16 10.16 2 12 2zm0 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z' },
  ];

  function handleAction(id) {
    if (id === 'combat') {
      onBattle?.();
    } else {
      // TODO: trigger LLM action
      console.log('action', id);
    }
  }

  function handleSend() {
    if (!inputText.trim()) return;
    // TODO: send to LLM backend
    console.log('player input:', inputText);
    inputText = '';
  }

  function handleKeydown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }

  // Derived HP percentage for bar width
  let hpPct = $derived(Math.max(0, Math.min(100, (charHp / charMaxHp) * 100)));
  let mpPct = $derived(Math.max(0, Math.min(100, (charMp / charMaxMp) * 100)));

  // HP bar color based on percentage
  let hpColor = $derived(
    hpPct > 50 ? 'var(--hp-full)' : hpPct > 25 ? 'var(--hp-mid)' : 'var(--hp-low)'
  );
</script>

<div class="game-screen">
  <!-- ── Top bar ─────────────────────────────────────────────────────────── -->
  <header class="game-topbar">
    <button class="topbar-back" onclick={onBack} aria-label="Torna al menù">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
      </svg>
    </button>

    <div class="campaign-label">
      <svg class="camp-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M9 3H7v2H5V3H3v6h2v11h14V9h2V3h-2v2h-2V3h-2v2h-2V3H9zm7 16H8V9h8v10z" />
      </svg>
      <span class="camp-name">{campaign.title ?? 'La Piaga di Ravenloft'}</span>
    </div>

    <div class="char-stats">
      <!-- HP bar -->
      <div class="stat-block" title="Punti Vita">
        <span class="stat-label">HP</span>
        <div class="stat-bar" style="--bar-color: {hpColor}">
          <div class="stat-fill" style="width: {hpPct}%"></div>
        </div>
        <span class="stat-value">{charHp}/{charMaxHp}</span>
      </div>

      <!-- MP bar -->
      <div class="stat-block" title="Punti Magia">
        <span class="stat-label">MP</span>
        <div class="stat-bar" style="--bar-color: var(--mp-color)">
          <div class="stat-fill" style="width: {mpPct}%"></div>
        </div>
        <span class="stat-value">{charMp}/{charMaxMp}</span>
      </div>
    </div>

    <div class="char-name">
      <span class="char-label">{campaign.charName ?? 'Eldrin'}</span>
      <span class="char-meta">{campaign.charClass ?? 'Mago'} Lv.{campaign.charLevel ?? 12}</span>
    </div>
  </header>

  <!-- ── Main area ──────────────────────────────────────────────────────── -->
  <main class="game-main">
    <!-- Scene illustration placeholder -->
    <div class="scene-art" aria-label="Scena attuale">
      <div class="scene-placeholder" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M9 3H7v2H5V3H3v6h2v11h14V9h2V3h-2v2h-2V3h-2v2h-2V3H9zm7 16H8V9h8v10z" />
        </svg>
        <span>Scena in generazione…</span>
      </div>
      <!-- Atmospheric gradient overlay -->
      <div class="scene-fade" aria-hidden="true"></div>
    </div>

    <!-- Narrative text panel -->
    <div class="narrative-panel">
      <div class="narrative-scroll" aria-live="polite" aria-label="Narrazione">
        {#each narrative.split('\n').filter(Boolean) as paragraph}
          <p class="narrative-text">{paragraph}</p>
        {/each}
      </div>
    </div>
  </main>

  <!-- ── Action area ──────────────────────────────────────────────────── -->
  <footer class="game-footer">
    <!-- Quick-action buttons -->
    <div class="quick-actions" role="toolbar" aria-label="Azioni rapide">
      {#each QUICK_ACTIONS as action}
        <button
          class="action-btn"
          class:combat={action.id === 'combat'}
          onclick={() => handleAction(action.id)}
          aria-label={action.label}
        >
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d={action.icon} />
          </svg>
          <span>{action.label}</span>
        </button>
      {/each}
    </div>

    <!-- Free-text input -->
    <div class="input-row">
      <textarea
        class="game-input"
        bind:value={inputText}
        onkeydown={handleKeydown}
        placeholder="Descrivi la tua azione…"
        rows="1"
        aria-label="Inserisci azione"
      ></textarea>
      <button class="send-btn" onclick={handleSend} disabled={!inputText.trim()} aria-label="Invia azione">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" />
        </svg>
      </button>
    </div>
  </footer>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  // ── CSS custom properties (bridging SCSS → dynamic inline styles) ────────────
  :global(.game-screen) {
    --hp-full: #{$hp-full};
    --hp-mid:  #{$hp-mid};
    --hp-low:  #{$hp-low};
    --mp-color: #{$mp-color};
  }

  // ── Page shell ───────────────────────────────────────────────────────────────
  .game-screen {
    height: 100vh;
    min-height: 100vh;
    background: $color-bg-page;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  // ── Top bar ──────────────────────────────────────────────────────────────────
  .game-topbar {
    height: $topbar-height;
    flex-shrink: 0;
    background: $color-bg-page;
    border-bottom: 1px solid $color-border-subtle;
    display: flex;
    align-items: center;
    gap: $space-6;
    padding: 0 $space-9;
    z-index: $z-topbar;
  }

  .topbar-back {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-md;
    cursor: pointer;
    color: $color-accent;
    flex-shrink: 0;
    transition: background $transition-base;

    svg { width: 18px; height: 18px; }
    &:hover { background: $color-surface-elevated; }
  }

  .campaign-label {
    display: flex;
    align-items: center;
    gap: $space-2;
    flex: 1;
    min-width: 0;
  }

  .camp-icon {
    width: 18px;
    height: 18px;
    color: $color-accent;
    flex-shrink: 0;
  }

  .camp-name {
    font-family: $font-sans;
    font-size: $font-size-game-ui;
    font-weight: $font-weight-bold;
    color: $white;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  // ── HP/MP bars ───────────────────────────────────────────────────────────────
  .char-stats {
    display: flex;
    flex-direction: column;
    gap: 5px;
    min-width: 180px;
  }

  .stat-block {
    display: flex;
    align-items: center;
    gap: $space-2;
  }

  .stat-label {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-bold;
    letter-spacing: 1px;
    color: $color-text-secondary;
    width: 20px;
    text-align: right;
  }

  .stat-bar {
    flex: 1;
    height: 6px;
    background: $color-hp-bg;
    border-radius: 3px;
    overflow: hidden;
  }

  .stat-fill {
    height: 100%;
    background: var(--bar-color);
    border-radius: 3px;
    transition: width 0.4s ease;
  }

  .stat-value {
    font-family: $font-sans;
    font-size: 11px;
    color: $color-text-secondary;
    min-width: 44px;
    text-align: right;
  }

  // ── Character name (right side of topbar) ────────────────────────────────────
  .char-name {
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 2px;
  }

  .char-label {
    font-family: $font-sans;
    font-size: $font-size-game-ui;
    font-weight: $font-weight-bold;
    color: $white;
  }

  .char-meta {
    font-family: $font-sans;
    font-size: 11px;
    color: $color-accent;
  }

  // ── Main area ─────────────────────────────────────────────────────────────────
  .game-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    max-width: $game-max-width;
    width: 100%;
    margin: 0 auto;
  }

  // ── Scene art ────────────────────────────────────────────────────────────────
  .scene-art {
    flex-shrink: 0;
    height: $game-scene-height;
    position: relative;
    background: $color-bg;
    overflow: hidden;
  }

  .scene-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: $space-3;
    color: rgba($gold-500, 0.20);

    svg {
      width: 48px;
      height: 48px;
    }

    span {
      font-family: $font-sans;
      font-size: $font-size-caption;
      color: rgba($cream, 0.25);
      font-style: italic;
    }
  }

  .scene-fade {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60%;
    background: linear-gradient(to bottom, transparent, $color-bg-page);
    pointer-events: none;
  }

  // ── Narrative panel ──────────────────────────────────────────────────────────
  .narrative-panel {
    flex: 1;
    overflow-y: auto;
    padding: $space-7 $space-9;

    &::-webkit-scrollbar {
      width: 4px;
    }
    &::-webkit-scrollbar-track {
      background: transparent;
    }
    &::-webkit-scrollbar-thumb {
      background: $color-border;
      border-radius: 2px;
    }
  }

  .narrative-scroll {
    display: flex;
    flex-direction: column;
    gap: $space-5;
  }

  .narrative-text {
    font-family: $font-sans;
    font-size: $font-size-game-body;
    line-height: 1.7;
    color: $color-text-primary;
    margin: 0;
  }

  // ── Footer ───────────────────────────────────────────────────────────────────
  .game-footer {
    flex-shrink: 0;
    background: $color-surface;
    border-top: 1px solid $color-border-subtle;
    padding: $space-5 $space-9;
    display: flex;
    flex-direction: column;
    gap: $space-4;
    max-width: $game-max-width;
    width: 100%;
    margin: 0 auto;
  }

  // ── Quick actions ─────────────────────────────────────────────────────────────
  .quick-actions {
    display: flex;
    gap: $space-3;
  }

  .action-btn {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    padding: $space-3 $space-2;
    background: $color-surface-elevated;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 11px;
    font-weight: $font-weight-semibold;
    letter-spacing: 0.5px;
    color: $color-text-primary;
    transition: background $transition-base, border-color $transition-base, color $transition-base;

    svg {
      width: 18px;
      height: 18px;
    }

    &:hover {
      background: $color-border;
      border-color: $color-border;
      color: $color-accent;
    }

    &.combat {
      border-color: rgba($red-400, 0.35);
      color: $red-400;

      &:hover {
        background: rgba($red-500, 0.12);
        border-color: $red-400;
      }
    }
  }

  // ── Input row ────────────────────────────────────────────────────────────────
  .input-row {
    display: flex;
    gap: $space-3;
    align-items: flex-end;
  }

  .game-input {
    flex: 1;
    resize: none;
    background: $color-bg-page;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    padding: $space-4 $space-5;
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-primary;
    line-height: 1.5;
    min-height: 44px;
    max-height: 120px;
    transition: border-color $transition-base;
    field-sizing: content;

    &::placeholder {
      color: $color-placeholder;
    }

    &:focus {
      outline: none;
      border-color: $color-border-focus;
    }
  }

  .send-btn {
    width: 44px;
    height: 44px;
    flex-shrink: 0;
    background: $color-btn-primary-bg;
    border: none;
    border-radius: $radius-md;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: $color-btn-primary-text;
    transition: $transition-btn;

    svg {
      width: 20px;
      height: 20px;
    }

    &:hover:not(:disabled) {
      background: $color-btn-primary-hover-bg;
      box-shadow: $glow-btn-primary;
    }

    &:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }
  }
</style>
