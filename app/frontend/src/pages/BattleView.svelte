<script>
  /**
   * campaign  — active campaign object
   * onBack    — return to GameScreen (battle ended)
   */
  let { campaign = {}, onBack } = $props();

  // ── Demo combat state ─────────────────────────────────────────────────────────
  let playerHp    = $state(62);
  const playerMaxHp = 80;
  let playerMp    = $state(24);
  const playerMaxMp = 30;

  let enemyHp     = $state(95);
  const enemyMaxHp = 140;

  let turn        = $state('player'); // 'player' | 'enemy' | 'end'
  let combatLog   = $state([
    { id: 1, type: 'system',  text: "Un Vampiro Spadaccino emerge dall'oscurità!" },
    { id: 2, type: 'enemy',   text: "Il Vampiro ti fissa con occhi ardenti di odio." },
  ]);

  const ENEMY = {
    name: 'Vampiro Spadaccino',
    type: 'Non-Morto · CR 5',
    icon: 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z',
  };

  const ACTIONS = [
    { id: 'attack',    label: 'Attacca',  icon: 'M7.5 5.6L10 7 8.6 4.5 10 2 7.5 3.4 5 2l1.4 2.5L5 7zm12 9.8L17 14l1.4 2.5L17 19l2.5-1.4L22 19l-1.4-2.5L22 14zM22 2l-2.5 1.4L17 2l1.4 2.5L17 7l2.5-1.4L22 7l-1.4-2.5zm-7.63 5.29a1.5 1.5 0 00-2.12 0L3 16.54V21h4.46l9.25-9.25a1.5 1.5 0 000-2.12l-2.34-2.34z', variant: 'primary' },
    { id: 'spell',     label: 'Magia',    icon: 'M12 2l2.09 6.43H21l-5.47 3.97 2.09 6.43L12 14.9l-5.62 3.93 2.09-6.43L3 8.43h6.91z', variant: 'magic' },
    { id: 'item',      label: 'Oggetto',  icon: 'M20 6h-2.18c.07-.44.18-.88.18-1.36C18 2.51 15.49 0 12 0 8.51 0 6 2.51 6 4.64c0 .48.11.92.18 1.36H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-8-4c1.84 0 3 1.16 3 2.64 0 .49-.27.92-.55 1.36h-4.9C9.27 5.56 9 5.13 9 4.64 9 3.16 10.16 2 12 2zm0 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z', variant: 'neutral' },
    { id: 'flee',      label: 'Fuggi',    icon: 'M13.49 5.48c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm-3.6 13.9l1-4.4 2.1 2v6h2v-7.5l-2.1-2 .6-3c1.3 1.5 3.3 2.5 5.5 2.5v-2c-1.9 0-3.5-1-4.3-2.4l-1-1.6c-.4-.6-1-1-1.7-1-.3 0-.5.1-.8.1l-5.2 2.2v4.7h2v-3.4l1.8-.7-1.6 8.1-4.9-1-.4 2 7 1.4z', variant: 'danger' },
  ];

  let logEndRef;
  let logId = 4;

  function addLog(type, text) {
    combatLog = [...combatLog, { id: ++logId, type, text }];
    // Auto-scroll to bottom
    setTimeout(() => logEndRef?.scrollIntoView({ behavior: 'smooth', block: 'end' }), 30);
  }

  function handleAction(id) {
    if (turn !== 'player') return;

    if (id === 'attack') {
      const dmg = Math.floor(Math.random() * 10) + 5;
      enemyHp = Math.max(0, enemyHp - dmg);
      addLog('player', `Attacchi con la tua spada e infliggi ${dmg} danni al ${ENEMY.name}!`);
      if (enemyHp <= 0) {
        turn = 'end';
        addLog('system', `Vittoria! Il ${ENEMY.name} è stato sconfitto.`);
        return;
      }
    } else if (id === 'spell') {
      if (playerMp < 5) { addLog('system', 'Non hai abbastanza Punti Magia!'); return; }
      const dmg = Math.floor(Math.random() * 15) + 8;
      playerMp = Math.max(0, playerMp - 5);
      enemyHp  = Math.max(0, enemyHp - dmg);
      addLog('player', `Lanci un incantesimo di fuoco — ${dmg} danni di fuoco! (−5 MP)`);
    } else if (id === 'item') {
      const heal = Math.floor(Math.random() * 10) + 10;
      playerHp = Math.min(playerMaxHp, playerHp + heal);
      addLog('player', `Usi una Pozione di Cura e recuperi ${heal} HP.`);
    } else if (id === 'flee') {
      addLog('system', 'Cerchi di fuggire dalla battaglia…');
      setTimeout(() => onBack?.(), 1200);
      return;
    }

    if (enemyHp <= 0) { turn = 'end'; return; }

    // Enemy turn
    turn = 'enemy';
    setTimeout(() => {
      const dmg = Math.floor(Math.random() * 8) + 4;
      playerHp = Math.max(0, playerHp - dmg);
      addLog('enemy', `Il ${ENEMY.name} ti attacca con le artigli — ${dmg} danni!`);
      if (playerHp <= 0) {
        turn = 'end';
        addLog('system', 'Sei stato sconfitto. La campagna è perduta…');
      } else {
        turn = 'player';
        addLog('system', 'Il tuo turno. Cosa fai?');
      }
    }, 900);
  }

  // Derived percentages
  let playerHpPct = $derived(Math.max(0, Math.min(100, (playerHp / playerMaxHp) * 100)));
  let playerMpPct = $derived(Math.max(0, Math.min(100, (playerMp / playerMaxMp) * 100)));
  let enemyHpPct  = $derived(Math.max(0, Math.min(100, (enemyHp  / enemyMaxHp)  * 100)));

  let playerHpColor = $derived(playerHpPct > 50 ? 'var(--hp-full)' : playerHpPct > 25 ? 'var(--hp-mid)' : 'var(--hp-low)');
  let enemyHpColor  = $derived(enemyHpPct  > 50 ? 'var(--hp-full)' : enemyHpPct  > 25 ? 'var(--hp-mid)' : 'var(--hp-low)');
</script>

<div class="battle-view">
  <!-- ── Top bar ─────────────────────────────────────────────────────────── -->
  <header class="battle-topbar">
    <button class="back-btn" onclick={onBack} aria-label="Torna alla schermata principale">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
      </svg>
    </button>

    <div class="battle-title-wrap">
      <span class="battle-label">BATTAGLIA</span>
      {#if turn === 'player'}
        <span class="turn-badge player-turn">Il tuo turno</span>
      {:else if turn === 'enemy'}
        <span class="turn-badge enemy-turn">Turno nemico</span>
      {:else}
        <span class="turn-badge end-turn">{playerHp > 0 ? 'Vittoria' : 'Sconfitta'}</span>
      {/if}
    </div>

    <div class="topbar-spacer"></div>
  </header>

  <!-- ── Combat area ─────────────────────────────────────────────────────── -->
  <div class="combat-area">
    <!-- Enemy card -->
    <div class="combatant-card enemy-card">
      <div class="combatant-portrait enemy-portrait" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
        </svg>
      </div>
      <div class="combatant-info">
        <div class="combatant-header">
          <span class="combatant-name">{ENEMY.name}</span>
          <span class="combatant-type">{ENEMY.type}</span>
        </div>
        <div class="hp-bar-row">
          <span class="hp-label">HP</span>
          <div class="hp-track">
            <div class="hp-fill" style="width: {enemyHpPct}%; background: {enemyHpColor}"></div>
          </div>
          <span class="hp-value">{enemyHp}/{enemyMaxHp}</span>
        </div>
      </div>
    </div>

    <!-- VS divider -->
    <div class="vs-divider" aria-hidden="true">
      <span>VS</span>
    </div>

    <!-- Player card -->
    <div class="combatant-card player-card">
      <div class="combatant-portrait player-portrait" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
        </svg>
      </div>
      <div class="combatant-info">
        <div class="combatant-header">
          <span class="combatant-name">{campaign.charName ?? 'Eldrin'}</span>
          <span class="combatant-type">{campaign.charClass ?? 'Mago'} · Lv.{campaign.charLevel ?? 12}</span>
        </div>
        <div class="hp-bar-row">
          <span class="hp-label">HP</span>
          <div class="hp-track">
            <div class="hp-fill" style="width: {playerHpPct}%; background: {playerHpColor}"></div>
          </div>
          <span class="hp-value">{playerHp}/{playerMaxHp}</span>
        </div>
        <div class="hp-bar-row">
          <span class="hp-label">MP</span>
          <div class="hp-track">
            <div class="hp-fill mp-fill" style="width: {playerMpPct}%"></div>
          </div>
          <span class="hp-value">{playerMp}/{playerMaxMp}</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ── Combat log ──────────────────────────────────────────────────────── -->
  <div class="combat-log" aria-live="polite" aria-label="Registro di combattimento">
    {#each combatLog as entry (entry.id)}
      <p class="log-entry {entry.type}">{entry.text}</p>
    {/each}
    <div bind:this={logEndRef}></div>
  </div>

  <!-- ── Action buttons ──────────────────────────────────────────────────── -->
  <div class="action-panel" role="toolbar" aria-label="Azioni in battaglia">
    {#each ACTIONS as action}
      <button
        class="battle-action {action.variant}"
        onclick={() => handleAction(action.id)}
        disabled={turn !== 'player'}
        aria-label={action.label}
      >
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d={action.icon} />
        </svg>
        <span>{action.label}</span>
      </button>
    {/each}
  </div>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  :global(.battle-view) {
    --hp-full:  #{$hp-full};
    --hp-mid:   #{$hp-mid};
    --hp-low:   #{$hp-low};
    --mp-color: #{$mp-color};
  }

  // ── Page shell ───────────────────────────────────────────────────────────────
  .battle-view {
    height: 100vh;
    background: $color-bg-page;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    max-width: $game-max-width;
    margin: 0 auto;
    width: 100%;
  }

  // ── Top bar ──────────────────────────────────────────────────────────────────
  .battle-topbar {
    height: $topbar-height;
    flex-shrink: 0;
    background: $color-bg-page;
    border-bottom: 1px solid $color-border-subtle;
    display: flex;
    align-items: center;
    padding: 0 $space-9;
    gap: $space-6;
  }

  .back-btn {
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

  .battle-title-wrap {
    display: flex;
    align-items: center;
    gap: $space-5;
    flex: 1;
  }

  .battle-label {
    font-family: $font-serif;
    font-size: $font-size-game-ui;
    font-weight: $font-weight-black;
    letter-spacing: 2px;
    color: $color-accent;
  }

  .turn-badge {
    font-family: $font-sans;
    font-size: 11px;
    font-weight: $font-weight-bold;
    letter-spacing: 0.5px;
    padding: 3px $space-4;
    border-radius: 999px;

    &.player-turn { background: rgba($hp-full, 0.18); color: $hp-full; }
    &.enemy-turn  { background: rgba($red-400, 0.18); color: $red-400; }
    &.end-turn    { background: rgba($gold-500, 0.18); color: $color-accent; }
  }

  .topbar-spacer { flex: 1; }

  // ── Combat area ──────────────────────────────────────────────────────────────
  .combat-area {
    flex-shrink: 0;
    display: flex;
    align-items: stretch;
    gap: $space-4;
    padding: $space-6 $space-9;
    border-bottom: 1px solid $color-border-subtle;
  }

  .combatant-card {
    flex: 1;
    display: flex;
    gap: $space-5;
    align-items: flex-start;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-lg;
    padding: $space-6;
    transition: border-color $transition-base;
  }

  .enemy-card  { border-color: rgba($red-400, 0.25); }
  .player-card { border-color: rgba($hp-full, 0.20); }

  .combatant-portrait {
    width: 52px;
    height: 52px;
    border-radius: $radius-md;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;

    svg {
      width: 28px;
      height: 28px;
    }
  }

  .enemy-portrait  { background: rgba($red-400, 0.14); color: $red-400; }
  .player-portrait { background: rgba($gold-500, 0.12); color: $color-accent; }

  .combatant-info {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: $space-3;
  }

  .combatant-header {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .combatant-name {
    font-family: $font-sans;
    font-size: 15px;
    font-weight: $font-weight-bold;
    color: $white;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .combatant-type {
    font-family: $font-sans;
    font-size: 11px;
    color: $color-text-secondary;
  }

  // ── HP bars ───────────────────────────────────────────────────────────────────
  .hp-bar-row {
    display: flex;
    align-items: center;
    gap: $space-2;
  }

  .hp-label {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-bold;
    letter-spacing: 1px;
    color: $color-text-secondary;
    width: 20px;
    text-align: right;
  }

  .hp-track {
    flex: 1;
    height: 8px;
    background: $color-hp-bg;
    border-radius: 4px;
    overflow: hidden;
  }

  .hp-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 0.5s ease;
  }

  .mp-fill {
    background: $mp-color !important;
  }

  .hp-value {
    font-family: $font-sans;
    font-size: 11px;
    color: $color-text-secondary;
    min-width: 48px;
    text-align: right;
  }

  // ── VS divider ────────────────────────────────────────────────────────────────
  .vs-divider {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;

    span {
      font-family: $font-serif;
      font-size: 13px;
      font-weight: $font-weight-black;
      letter-spacing: 2px;
      color: $color-text-secondary;
    }
  }

  // ── Combat log ────────────────────────────────────────────────────────────────
  .combat-log {
    flex: 1;
    overflow-y: auto;
    padding: $space-6 $space-9;
    display: flex;
    flex-direction: column;
    gap: $space-3;

    &::-webkit-scrollbar { width: 4px; }
    &::-webkit-scrollbar-track { background: transparent; }
    &::-webkit-scrollbar-thumb { background: $color-border; border-radius: 2px; }
  }

  .log-entry {
    font-family: $font-sans;
    font-size: $font-size-body;
    line-height: 1.55;
    margin: 0;
    padding: $space-3 $space-5;
    border-radius: $radius-md;

    &.system {
      color: $color-accent;
      font-style: italic;
      background: rgba($gold-500, 0.06);
      border-left: 2px solid $color-accent;
    }

    &.player {
      color: $color-text-primary;
      background: rgba($hp-full, 0.06);
      border-left: 2px solid $hp-full;
    }

    &.enemy {
      color: $color-text-primary;
      background: rgba($red-400, 0.06);
      border-left: 2px solid $red-400;
    }
  }

  // ── Action panel ─────────────────────────────────────────────────────────────
  .action-panel {
    flex-shrink: 0;
    display: flex;
    gap: $space-3;
    padding: $space-5 $space-9;
    background: $color-surface;
    border-top: 1px solid $color-border-subtle;
  }

  .battle-action {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: $space-1 + 2px;
    padding: $space-4 $space-3;
    border-radius: $radius-md;
    border: 1px solid $color-border-subtle;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 12px;
    font-weight: $font-weight-bold;
    letter-spacing: 0.5px;
    transition: background $transition-base, border-color $transition-base, color $transition-base, transform $transition-fast;

    svg {
      width: 22px;
      height: 22px;
    }

    &:active:not(:disabled) { transform: translateY(1px); }

    &:disabled {
      opacity: 0.30;
      cursor: not-allowed;
    }

    &.primary {
      background: $color-btn-primary-bg;
      border-color: $color-btn-primary-bg;
      color: $color-btn-primary-text;

      &:hover:not(:disabled) {
        background: $color-btn-primary-hover-bg;
        box-shadow: $glow-btn-primary;
      }
    }

    &.magic {
      background: rgba($mp-color, 0.14);
      border-color: rgba($mp-color, 0.30);
      color: $mp-color;

      &:hover:not(:disabled) {
        background: rgba($mp-color, 0.24);
        border-color: $mp-color;
      }
    }

    &.neutral {
      background: $color-surface-elevated;
      color: $color-text-primary;

      &:hover:not(:disabled) {
        background: $color-border;
        border-color: $color-border;
        color: $color-accent;
      }
    }

    &.danger {
      background: rgba($red-500, 0.10);
      border-color: rgba($red-400, 0.30);
      color: $red-400;

      &:hover:not(:disabled) {
        background: rgba($red-500, 0.20);
        border-color: $red-400;
      }
    }
  }
</style>
