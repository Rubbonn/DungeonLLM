<script lang="ts">
  import type { TemplateCampaign } from '../lib/types.js';

  /**
   * onBack  — navigate back to home
   * onStart — called with selected campaign to begin game
   */
  interface Props {
    onBack?: () => void;
    onStart?: (campaign: TemplateCampaign) => void;
  }

  let { onBack, onStart }: Props = $props();

  // ── Tab state ─────────────────────────────────────────────────────────────────
  type TabName = 'template' | 'bozze';
  let activeTab = $state<TabName>('template');

  // ── Campaigns data ────────────────────────────────────────────────────────────
  const TEMPLATES: TemplateCampaign[] = [
    {
      id: 'ravenloft',
      title: "L'Ombra di Ravenloft",
      desc: "Un'avventura gotica tra nebbie perenni e castelli infestati. Affronta il male ancestrale che dimora nelle terre di Barovia.",
      players: '3-5 Giocatori',
      level: 'Livello 1-10',
      badge: 'CONSIGLIATO',
      badgeColor: 'gold',
      thumbColor: '#1a2030',
      draft: false,
    },
    {
      id: 'underdark',
      title: 'I Misteri di Underdark',
      desc: 'Esplora le profondità della terra in cerca di antichi manufatti. Le civiltà sotterranee nascondono segreti pericolosi.',
      players: '4-6 Giocatori',
      level: 'Livello 5-15',
      badge: null,
      badgeColor: null,
      thumbColor: '#0d2020',
      draft: false,
    },
    {
      id: 'cenere',
      title: 'Il Deserto di Cenere',
      desc: 'Descrizione in fase di completamento… Ambientazione post-apocalittica fantasy.',
      players: null,
      level: null,
      badge: 'BOZZA',
      badgeColor: 'muted',
      thumbColor: '#1e1e1e',
      draft: true,
    },
  ];

  const BOZZE: TemplateCampaign[] = TEMPLATES.filter(t => t.draft);
  const DISPLAYED = $derived<TemplateCampaign[]>(activeTab === 'template' ? TEMPLATES : BOZZE);

  function handleStart(campaign: TemplateCampaign): void {
    if (campaign.draft) return;
    onStart?.(campaign);
  }
</script>

<div class="nc-page">
  <!-- ── Top bar ─────────────────────────────────────────────────────────── -->
  <header class="nc-topbar">
    <div class="nc-logo">
      <div class="nc-logo-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M9 3H7v2H5V3H3v6h2v11h14V9h2V3h-2v2h-2V3h-2v2h-2V3H9zm7 16H8V9h8v10z" />
        </svg>
      </div>
      <span class="nc-logo-title">Nuova Campagna</span>
    </div>

    <div class="nc-topbar-right">
      <button class="back-link" onclick={onBack}>
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
        </svg>
        Torna al Menu
      </button>
      <button class="new-btn" aria-label="Crea nuova campagna">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z" />
        </svg>
      </button>
    </div>
  </header>

  <!-- ── Tabs ───────────────────────────────────────────────────────────── -->
  <div class="nc-tabs">
    <button
      class="tab-btn"
      class:active={activeTab === 'template'}
      onclick={() => (activeTab = 'template')}
    >Template</button>
    <button
      class="tab-btn"
      class:active={activeTab === 'bozze'}
      onclick={() => (activeTab = 'bozze')}
    >Le Mie Bozze</button>
    <div class="tab-divider" aria-hidden="true"></div>
  </div>

  <!-- ── Campaign list ─────────────────────────────────────────────────── -->
  <div class="nc-list">
    {#each DISPLAYED as camp (camp.id)}
      <article class="camp-card" class:draft={camp.draft} aria-label={camp.title}>
        <!-- Thumbnail -->
        <div class="camp-thumb" style="background: {camp.thumbColor};" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M9 3H7v2H5V3H3v6h2v11h14V9h2V3h-2v2h-2V3h-2v2h-2V3H9zm7 16H8V9h8v10z" />
          </svg>
        </div>

        <!-- Info -->
        <div class="camp-info">
          <div class="camp-title-row">
            <h2 class="camp-title" class:draft-title={camp.draft}>{camp.title}</h2>
            {#if camp.badge}
              <span class="camp-badge {camp.badgeColor}">{camp.badge}</span>
            {/if}
          </div>
          <p class="camp-desc" class:draft-desc={camp.draft}>{camp.desc}</p>
          {#if camp.players || camp.level}
            <div class="camp-meta">
              {#if camp.players}
                <span class="meta-item">
                  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z" />
                  </svg>
                  {camp.players}
                </span>
              {/if}
              {#if camp.level}
                <span class="meta-item">
                  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z" />
                  </svg>
                  {camp.level}
                </span>
              {/if}
            </div>
          {/if}

          <!-- Actions row -->
          <div class="camp-actions">
            <div class="camp-actions-left">
              <button class="btn-secondary">
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z" />
                </svg>
                {camp.draft ? 'Continua Modifica' : 'Modifica'}
              </button>
              <button class="btn-danger">
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z" />
                </svg>
                Elimina
              </button>
            </div>
            <button
              class="btn-start"
              class:disabled={camp.draft}
              onclick={() => handleStart(camp)}
              disabled={camp.draft}
              aria-label="Inizia {camp.title}"
            >
              {#if camp.draft}
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z" />
                </svg>
              {:else}
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M8 5v14l11-7z" />
                </svg>
              {/if}
              Inizia
            </button>
          </div>
        </div>
      </article>
    {/each}
  </div>

  <!-- ── Footer hint ────────────────────────────────────────────────────── -->
  <footer class="nc-footer">
    <p>Seleziona un template per iniziare la tua avventura o crea una nuova campagna da zero.</p>
  </footer>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  .nc-page {
    min-height: 100vh;
    background: $color-bg-page;
    color: $color-text-primary;
    display: flex;
    flex-direction: column;
  }

  // ── Top bar ───────────────────────────────────────────────────────────────────
  .nc-topbar {
    height: $topbar-height;
    flex-shrink: 0;
    background: $color-bg-page;
    border-bottom: 1px solid $color-border-subtle;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 $space-9;
    gap: $space-6;
  }

  .nc-logo {
    display: flex;
    align-items: center;
    gap: $space-3;
  }

  .nc-logo-icon {
    width: 32px;
    height: 32px;
    background: $color-accent;
    border-radius: $radius-sm;
    display: flex;
    align-items: center;
    justify-content: center;
    color: $dark-700;
    svg { width: 18px; height: 18px; }
  }

  .nc-logo-title {
    font-family: $font-sans;
    font-size: 18px;
    font-weight: $font-weight-black;
    color: $white;
  }

  .nc-topbar-right {
    display: flex;
    align-items: center;
    gap: $space-4;
  }

  .back-link {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-secondary;
    padding: 0;
    transition: color $transition-base;
    svg { width: 16px; height: 16px; }
    &:hover { color: $white; }
  }

  .new-btn {
    width: 34px;
    height: 34px;
    background: $color-surface;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: $white;
    transition: background $transition-base;
    svg { width: 18px; height: 18px; }
    &:hover { background: $color-surface-elevated; }
  }

  // ── Tabs ─────────────────────────────────────────────────────────────────────
  .nc-tabs {
    position: relative;
    display: flex;
    align-items: flex-end;
    gap: $space-2;
    padding: 0 $space-9;
    flex-shrink: 0;
  }

  .tab-divider {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: $color-border-subtle;
  }

  .tab-btn {
    position: relative;
    z-index: 1;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-body;
    font-weight: $font-weight-semibold;
    color: $color-text-secondary;
    padding: $space-5 $space-2 $space-4;
    transition: color $transition-base;

    &::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 2px;
      background: transparent;
      transition: background $transition-base;
    }

    &.active {
      color: $color-accent;
      &::after { background: $color-accent; }
    }

    &:hover:not(.active) { color: $color-text-primary; }
  }

  // ── Campaign list ─────────────────────────────────────────────────────────────
  .nc-list {
    flex: 1;
    max-width: $nc-max-width;
    width: 100%;
    margin: 0 auto;
    padding: $space-7 $space-9 $space-9;
    display: flex;
    flex-direction: column;
    gap: $space-5;
  }

  .camp-card {
    display: flex;
    gap: 0;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-lg;
    overflow: hidden;
    transition: border-color $transition-base, box-shadow $transition-base;

    &:hover:not(.draft) {
      border-color: $color-border;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);
    }

    &.draft {
      border-style: dashed;
      opacity: 0.80;
    }
  }

  // Thumbnail
  .camp-thumb {
    width: $nc-thumb-width;
    min-height: $nc-thumb-height;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    svg { width: 40px; height: 40px; color: rgba($cream, 0.15); }
  }

  // Info column
  .camp-info {
    flex: 1;
    min-width: 0;
    padding: $space-7 $space-8;
    display: flex;
    flex-direction: column;
    gap: $space-3;
  }

  .camp-title-row {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: $space-4;
  }

  .camp-title {
    font-family: $font-sans;
    font-size: 20px;
    font-weight: $font-weight-black;
    color: $color-accent;
    margin: 0;
    line-height: 1.2;
  }

  .draft-title { color: $color-text-primary; }

  .camp-badge {
    flex-shrink: 0;
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-black;
    letter-spacing: 0.5px;
    padding: 3px $space-3;
    border-radius: $radius-sm;
    white-space: nowrap;
    margin-top: 2px;

    &.gold  { background: $color-surface-elevated; border: 1px solid $color-accent; color: $color-accent; }
    &.muted { background: $color-surface-elevated; border: 1px solid $color-border; color: $color-text-secondary; }
  }

  .camp-desc {
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-primary;
    line-height: 1.55;
    margin: 0;
  }

  .draft-desc {
    font-style: italic;
    color: $color-text-secondary;
  }

  .camp-meta {
    display: flex;
    gap: $space-5;
  }

  .meta-item {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    font-family: $font-sans;
    font-size: $font-size-caption;
    color: $color-text-secondary;

    svg { width: 13px; height: 13px; color: $color-accent; }
  }

  // Actions row
  .camp-actions {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: $space-4;
    padding-top: $space-2;
    margin-top: auto;
  }

  .camp-actions-left {
    display: flex;
    gap: $space-3;
  }

  .btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    padding: $space-3 $space-6;
    background: $color-surface-elevated;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 13px;
    font-weight: $font-weight-bold;
    color: $white;
    transition: background $transition-base;
    svg { width: 14px; height: 14px; }
    &:hover { background: $color-border; }
  }

  .btn-danger {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    padding: $space-3 $space-5;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 13px;
    font-weight: $font-weight-bold;
    color: $color-text-secondary;
    transition: color $transition-base;
    svg { width: 14px; height: 14px; }
    &:hover { color: $red-400; }
  }

  .btn-start {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    padding: $space-3 $space-7;
    background: $color-btn-primary-bg;
    border: none;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 13px;
    font-weight: $font-weight-black;
    letter-spacing: 0.5px;
    color: $color-btn-primary-text;
    transition: $transition-btn;
    svg { width: 14px; height: 14px; }

    &:hover:not(:disabled):not(.disabled) {
      background: $color-btn-primary-hover-bg;
      box-shadow: $glow-btn-primary;
    }

    &:disabled, &.disabled {
      background: $color-surface-elevated;
      color: $color-text-secondary;
      cursor: not-allowed;
    }
  }

  // ── Footer ────────────────────────────────────────────────────────────────────
  .nc-footer {
    flex-shrink: 0;
    padding: $space-7 $space-9;
    text-align: center;
    border-top: 1px solid $color-border-subtle;

    p {
      font-family: $font-sans;
      font-size: $font-size-caption;
      color: $color-text-secondary;
      margin: 0;
    }
  }
</style>
