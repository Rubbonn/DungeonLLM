<script lang="ts">
  /**
   * open    — controls visibility of the panel
   * onClose — callback fired when × is clicked
   */
  interface RuleCard {
    id: string;
    source: string;
    title: string;
    body: string;
    uses: string;
    reset: string;
  }

  interface Props {
    open?: boolean;
    onClose?: () => void;
  }

  let { open = $bindable(false), onClose }: Props = $props();

  // ── Demo data matching screenshot ─────────────────────────────────────────────
  const RULES: RuleCard[] = [
    {
      id: 'divine-sense',
      source: 'SRD 5.1: PALADIN FEATURES',
      title: 'Divine Sense',
      body: "Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type of any being whose presence you sense, but not its identity.",
      uses: '1 + CHARISMA MODIFIER (MIN 1)',
      reset: 'LONG REST',
    },
  ];

  const STRATEGY_TIP: string =
    "Since you suspect undead in the mist, Divine Sense is a great choice. Note that it doesn't reveal creatures behind total cover, so the pillars might block your sense.";

  const RECENT_QUERIES: string[] = [
    'How does Smite work with Crits?',
    'Heavy Armor & Stealth disadvantage',
    'Aura of Protection range',
  ];

  const QUICK_TAGS: string[] = ['ACTION ECONOMY', 'CONDITIONS', 'SPELLS'];

  let searchText = $state<string>('');

  function handleSearch(): void {
    if (!searchText.trim()) return;
    // TODO: query rules LLM
    console.log('rules query:', searchText);
    searchText = '';
  }

  function handleKeydown(e: KeyboardEvent): void {
    if (e.key === 'Enter') handleSearch();
  }

  function handleRecentQuery(q: string): void {
    searchText = q;
    handleSearch();
  }
</script>

{#if open}
  <aside class="rules-panel" aria-label="Consulta Regole">
    <!-- Header -->
    <div class="panel-header">
      <div class="panel-title-row">
        <svg class="panel-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 14H8v-2h8v2zm0-4H8v-2h8v2zm0-4H8V6h8v2z" />
        </svg>
        <span class="panel-title">RULES CONSULTANT</span>
      </div>
      <button class="close-btn" onclick={onClose} aria-label="Chiudi consulta regole">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
        </svg>
      </button>
    </div>

    <!-- Scrollable body -->
    <div class="panel-body">
      <!-- Rule cards -->
      {#each RULES as rule (rule.id)}
        <div class="rule-card">
          <div class="rule-source-row">
            <div class="info-dot" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z" />
              </svg>
            </div>
            <span class="rule-source">{rule.source}</span>
          </div>
          <h3 class="rule-title">{rule.title}</h3>
          <p class="rule-body">{rule.body}</p>
          <div class="rule-meta">
            <span class="meta-row"><span class="meta-key">USES:</span> {rule.uses}</span>
            <span class="meta-row"><span class="meta-key">RESET:</span> {rule.reset}</span>
          </div>
        </div>
      {/each}

      <!-- Strategy tip -->
      <div class="tip-card">
        <div class="tip-header">
          <span class="tip-dot" aria-hidden="true"></span>
          <span class="tip-label">STRATEGY TIP</span>
        </div>
        <p class="tip-text">{STRATEGY_TIP}</p>
      </div>

      <!-- Recent queries -->
      <div class="recent-section">
        <span class="recent-heading">RECENT QUERIES</span>
        <ul class="recent-list">
          {#each RECENT_QUERIES as q}
            <li>
              <button class="recent-item" onclick={() => handleRecentQuery(q)}>
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M13 3c-4.97 0-9 4.03-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42C8.27 19.99 10.51 21 13 21c4.97 0 9-4.03 9-9s-4.03-9-9-9z" />
                </svg>
                {q}
              </button>
            </li>
          {/each}
        </ul>
      </div>
    </div>

    <!-- Search footer -->
    <div class="search-footer">
      <div class="search-row">
        <svg class="search-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" />
        </svg>
        <input
          class="search-input"
          type="text"
          placeholder="Ask about a rule..."
          bind:value={searchText}
          onkeydown={handleKeydown}
          aria-label="Cerca una regola"
        />
      </div>
      <div class="tag-row">
        {#each QUICK_TAGS as tag}
          <button class="tag-chip" onclick={() => handleRecentQuery(tag)}>{tag}</button>
        {/each}
      </div>
    </div>
  </aside>
{/if}

<style lang="scss">
  @use '../styles/variables' as *;

  // ── Panel shell ──────────────────────────────────────────────────────────────
  .rules-panel {
    width: $game-sidebar-width;
    flex-shrink: 0;
    background: $color-surface;
    border-left: 1px solid $color-border-subtle;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  // ── Header ───────────────────────────────────────────────────────────────────
  .panel-header {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: $space-5 $space-6;
    border-bottom: 1px solid $color-border-subtle;
    background: $color-surface;
  }

  .panel-title-row {
    display: flex;
    align-items: center;
    gap: $space-2;
  }

  .panel-icon {
    width: 16px;
    height: 16px;
    color: $color-accent;
    flex-shrink: 0;
  }

  .panel-title {
    font-family: $font-sans;
    font-size: 12px;
    font-weight: $font-weight-black;
    letter-spacing: 1.5px;
    color: $white;
    text-transform: uppercase;
  }

  .close-btn {
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: none;
    border: none;
    cursor: pointer;
    color: $color-text-secondary;
    border-radius: $radius-sm;
    transition: color $transition-base, background $transition-base;

    svg { width: 16px; height: 16px; }

    &:hover {
      color: $white;
      background: $color-surface-elevated;
    }
  }

  // ── Body ─────────────────────────────────────────────────────────────────────
  .panel-body {
    flex: 1;
    overflow-y: auto;
    padding: $space-5 $space-6;
    display: flex;
    flex-direction: column;
    gap: $space-4;

    &::-webkit-scrollbar { width: 3px; }
    &::-webkit-scrollbar-track { background: transparent; }
    &::-webkit-scrollbar-thumb { background: $color-border; border-radius: 2px; }
  }

  // ── Rule card ────────────────────────────────────────────────────────────────
  .rule-card {
    background: $rules-info-bg;
    border: 1px solid $rules-info-border;
    border-radius: $radius-lg;
    padding: $space-5 $space-5;
    display: flex;
    flex-direction: column;
    gap: $space-2;
  }

  .rule-source-row {
    display: flex;
    align-items: center;
    gap: $space-2;
  }

  .info-dot {
    width: 16px;
    height: 16px;
    color: $mp-color;
    flex-shrink: 0;

    svg { width: 16px; height: 16px; }
  }

  .rule-source {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-black;
    letter-spacing: 1px;
    color: $mp-color;
    text-transform: uppercase;
  }

  .rule-title {
    font-family: $font-sans;
    font-size: 15px;
    font-weight: $font-weight-black;
    color: $white;
    margin: 0;
    line-height: 1.2;
  }

  .rule-body {
    font-family: $font-sans;
    font-size: 12px;
    color: $color-text-primary;
    line-height: 1.55;
    margin: 0;
  }

  .rule-meta {
    display: flex;
    flex-direction: column;
    gap: 3px;
    margin-top: $space-1;
  }

  .meta-row {
    font-family: $font-sans;
    font-size: 10px;
    color: $color-text-secondary;
    letter-spacing: 0.3px;
  }

  .meta-key {
    color: $color-accent;
    font-weight: $font-weight-bold;
  }

  // ── Strategy tip ─────────────────────────────────────────────────────────────
  .tip-card {
    background: $rules-tip-bg;
    border: 1px solid $rules-tip-border;
    border-radius: $radius-lg;
    padding: $space-5;
    display: flex;
    flex-direction: column;
    gap: $space-2;
  }

  .tip-header {
    display: flex;
    align-items: center;
    gap: $space-2;
  }

  .tip-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: $rules-tip-color;
    flex-shrink: 0;
  }

  .tip-label {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-black;
    letter-spacing: 1px;
    color: $rules-tip-color;
    text-transform: uppercase;
  }

  .tip-text {
    font-family: $font-sans;
    font-size: 12px;
    font-style: italic;
    color: $color-text-primary;
    line-height: 1.55;
    margin: 0;
  }

  // ── Recent queries ────────────────────────────────────────────────────────────
  .recent-section {
    display: flex;
    flex-direction: column;
    gap: $space-2;
  }

  .recent-heading {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-black;
    letter-spacing: 1.5px;
    color: $color-text-secondary;
    text-transform: uppercase;
  }

  .recent-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .recent-item {
    display: flex;
    align-items: center;
    gap: $space-2;
    width: 100%;
    text-align: left;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 13px;
    color: $color-text-primary;
    padding: $space-2 $space-3;
    border-radius: $radius-sm;
    transition: background $transition-base, color $transition-base;

    svg {
      width: 13px;
      height: 13px;
      color: $color-accent;
      flex-shrink: 0;
    }

    &:hover {
      background: $color-surface-elevated;
      color: $color-accent;
    }
  }

  // ── Search footer ─────────────────────────────────────────────────────────────
  .search-footer {
    flex-shrink: 0;
    padding: $space-4 $space-6;
    border-top: 1px solid $color-border-subtle;
    display: flex;
    flex-direction: column;
    gap: $space-3;
    background: $color-bg-page;
  }

  .search-row {
    display: flex;
    align-items: center;
    gap: $space-2;
    background: $color-surface;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    padding: $space-2 $space-4;
    transition: border-color $transition-base;

    &:focus-within {
      border-color: $color-border-focus;
    }
  }

  .search-icon {
    width: 14px;
    height: 14px;
    color: $color-text-secondary;
    flex-shrink: 0;
  }

  .search-input {
    flex: 1;
    background: none;
    border: none;
    outline: none;
    font-family: $font-sans;
    font-size: 13px;
    color: $color-text-primary;
    min-width: 0;

    &::placeholder { color: $color-placeholder; }
  }

  .tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: $space-2;
  }

  .tag-chip {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-bold;
    letter-spacing: 0.5px;
    color: $color-accent;
    background: rgba($gold-500, 0.10);
    border: 1px solid rgba($gold-500, 0.22);
    border-radius: 999px;
    padding: 3px $space-3;
    cursor: pointer;
    transition: background $transition-base, border-color $transition-base;
    white-space: nowrap;

    &:hover {
      background: rgba($gold-500, 0.20);
      border-color: $color-accent;
    }
  }
</style>
