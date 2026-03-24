<script lang="ts">
  import RulesConsultant from '../components/RulesConsultant.svelte';
  import type {
    GameSession,
    AttrEntry,
    CharData,
    EquipmentItem,
    AbilityItem,
    InventoryItem,
    ChatMessage,
  } from '../lib/types.js';

  /**
   * campaign  — active game session info (title, charName, charClass, charLevel)
   * onBack    — navigate back to home
   * onBattle  — navigate to BattleView
   */
  interface Props {
    campaign?: GameSession;
    onBack?: () => void;
    onBattle?: () => void;
  }

  let { campaign = {}, onBack, onBattle }: Props = $props();

  // ── Character data (demo) ─────────────────────────────────────────────────────
  const CHAR = $derived.by<CharData>(() => ({
    name:    campaign.charName  ?? 'Kaelen Nightshade',
    cls:     campaign.charClass ?? 'Rogue',
    level:   campaign.charLevel ?? 12,
    hp: 85,  maxHp:   100,
    mana: 20, maxMana: 50,
    attrs: [
      { key: 'STR', value: 14, icon: 'M20.57 14.86L22 13.43 20.57 12 17 15.57 8.43 7 12 3.43 10.57 2 9.14 3.43 7.71 2 5.57 4.14 4.14 2.71 2.71 4.14l1.43 1.43L2 7.71l1.43 1.43L2 10.57 3.43 12 7 8.43 15.57 17 12 20.57 13.43 22l1.43-1.43L16.29 22l2.14-2.14-1.43-1.43L19.43 17l-1.43-1.43z' },
      { key: 'DEX', value: 18, icon: 'M13.49 5.48c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm-3.6 13.9l1-4.4 2.1 2v6h2v-7.5l-2.1-2 .6-3c1.3 1.5 3.3 2.5 5.5 2.5v-2c-1.9 0-3.5-1-4.3-2.4l-1-1.6c-.4-.6-1-1-1.7-1-.3 0-.5.1-.8.1l-5.2 2.2v4.7h2v-3.4l1.8-.7-1.6 8.1-4.9-1-.4 2 7 1.4z' },
      { key: 'CON', value: 12, icon: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z' },
      { key: 'INT', value: 10, icon: 'M12 3L1 9l4 2.18V17c0 .55.23 1.05.6 1.42C7.17 19.1 9.46 21 12 21s4.83-1.9 6.4-2.58c.37-.37.6-.87.6-1.42v-5.82L20 9.18V17h2V9L12 3z' },
      { key: 'WIS', value: 14, icon: 'M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z' },
      { key: 'CHA', value: 16, icon: 'M12 1L9.5 8.5H2l6 4.5-2.5 7.5L12 16l6.5 4.5-2.5-7.5 6-4.5h-7.5z' },
    ] satisfies AttrEntry[],
  }));

  const EQUIPMENT: EquipmentItem[] = [
    { id: 1, icon: 'M20.57 14.86L22 13.43 20.57 12 17 15.57 8.43 7 12 3.43 10.57 2 9.14 3.43 7.71 2 5.57 4.14 4.14 2.71 2.71 4.14l1.43 1.43L2 7.71l1.43 1.43L2 10.57 3.43 12 7 8.43 15.57 17 12 20.57 13.43 22l1.43-1.43L16.29 22l2.14-2.14-1.43-1.43L19.43 17l-1.43-1.43z', name: 'Nightshade Daggers', slot: 'Main / Off Hand', badge: '+2 Poison',  badgeColor: 'green' },
    { id: 2, icon: 'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z',                                                                                                                                                                                                                                                                               name: 'Shadow-weave Tunic',  slot: 'Chest Armor',   badge: '+5 Stealth', badgeColor: 'blue'  },
  ];

  const ABILITIES: AbilityItem[] = [
    { id: 1, name: 'Cunning Action', type: 'PASSIVE', desc: 'Bonus action for Dash, Disengage, or Hide.' },
    { id: 2, name: 'Sneak Attack',   type: 'COMBAT',  desc: '+3d6 damage on advantage hits.' },
  ];

  const INVENTORY_ITEMS: InventoryItem[] = [
    { id: 1, count: 3,    icon: 'M20 6h-2.18c.07-.44.18-.88.18-1.36C18 2.51 15.49 0 12 0 8.51 0 6 2.51 6 4.64c0 .48.11.92.18 1.36H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-8-4c1.84 0 3 1.16 3 2.64 0 .49-.27.92-.55 1.36h-4.9C9.27 5.56 9 5.13 9 4.64 9 3.16 10.16 2 12 2zm0 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z' },
    { id: 2, count: null, icon: 'M12.65 10C11.83 7.67 9.61 6 7 6c-3.31 0-6 2.69-6 6s2.69 6 6 6c2.61 0 4.83-1.67 5.65-4H17v4h4v-4h2v-4H12.65zM7 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z' },
    { id: 3, count: null, icon: 'M4 6H2v14c0 1.1.9 2 2 2h14v-2H4V6zm16-4H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-1 9H9V9h10v2zm-4 4H9v-2h6v2zm4-8H9V5h10v2z' },
    { id: 4, count: null, icon: 'M7.5 5.6L10 7 8.6 4.5 10 2 7.5 3.4 5 2l1.4 2.5L5 7zm12 9.8L17 14l1.4 2.5L17 19l2.5-1.4L22 19l-1.4-2.5L22 14zM22 2l-2.5 1.4L17 2l1.4 2.5L17 7l2.5-1.4L22 7l-1.4-2.5zm-7.63 5.29a1.5 1.5 0 00-2.12 0L3 16.54V21h4.46l9.25-9.25a1.5 1.5 0 000-2.12l-2.34-2.34z' },
  ];

  const ENCUMBRANCE: { current: number; max: number } = { current: 42, max: 120 };
  const GOLD = 1240;

  // ── Chat state ────────────────────────────────────────────────────────────────
  let messages = $state<ChatMessage[]>([
    {
      id: 1, role: 'master',
      text: '"The heavy iron doors creak open with a groan that echoes through the chamber, revealing a damp stone corridor illuminated only by flickering, soot-stained torches. The air is thick with the smell of rot and old moisture. From the darkness ahead, a low, guttural growl vibrates through the stone floor beneath your boots."',
      note: 'The shadows seem to dance with predatory intent.',
      check: 'PERCEPTION CHECK REQUIRED',
    },
    {
      id: 2, role: 'player',
      text: 'I draw my twin daggers and melt into the shadows, attempting to scout ahead without being seen. I want to identify what is making that noise.',
    },
    {
      id: 3, role: 'master',
      text: '"You roll a 17 for Stealth. Like a ghost, you slip from patch of shadow to patch of shadow. The growling stops for a moment, then resumes, accompanied by the sound of heavy chains rattling. Rounding the corner, you spot a massive, three-headed hound guarding a silver-bound chest. Its eyes are like burning coals in the gloom."',
    },
  ]);

  let inputText  = $state<string>('');
  let chatEndRef = $state<HTMLElement | null>(null);
  let msgId      = $state<number>(4);

  // ── Panel state ───────────────────────────────────────────────────────────────
  let rulesOpen = $state<boolean>(false);
  let equipOpen  = $state<boolean>(true);
  let abilOpen   = $state<boolean>(true);
  let invOpen    = $state<boolean>(true);

  function handleSend(): void {
    if (!inputText.trim()) return;
    messages = [...messages, { id: ++msgId, role: 'player', text: inputText.trim() }];
    inputText = '';
    setTimeout(() => chatEndRef?.scrollIntoView({ behavior: 'smooth', block: 'end' }), 40);
  }

  function handleKeydown(e: KeyboardEvent): void {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSend(); }
  }

  let hpPct   = $derived(Math.round((CHAR.hp   / CHAR.maxHp)   * 100));
  let manaPct = $derived(Math.round((CHAR.mana  / CHAR.maxMana) * 100));
  let encPct  = $derived(Math.round((ENCUMBRANCE.current / ENCUMBRANCE.max) * 100));
</script>

<div class="game-screen">

  <!-- ══ TOP BAR ════════════════════════════════════════════════════════════ -->
  <header class="game-topbar">
    <button class="logo-wrap" onclick={onBack} aria-label="Torna al menù">
      <div class="logo-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M9 3H7v2H5V3H3v6h2v11h14V9h2V3h-2v2h-2V3h-2v2h-2V3H9zm7 16H8V9h8v10z" />
        </svg>
      </div>
      <span class="logo-text">DungeonLLM</span>
    </button>

    <div class="topbar-center">
      <div class="info-pill">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm.31 14.71c-1.51-.32-2.72-1.3-2.72-2.81 0-1.79 1.49-2.69 3.66-3.21 1.95-.46 2.34-1.15 2.34-1.86 0-.53-.39-1.39-2.1-1.39-1.6 0-2.23.72-2.32 1.64H9.46c.1-1.7 1.36-2.66 2.86-2.97V5.5h2.34v1.67c1.52.29 2.72 1.16 2.73 2.77-.01 2.2-1.9 2.96-3.66 3.42-1.77.45-2.34.94-2.34 1.67 0 .84.79 1.43 2.1 1.43 1.38 0 1.9-.66 1.94-1.64h1.71c-.05 1.34-.87 2.57-2.49 2.97V18.5H11.9v-1.79z" />
        </svg>
        <span>{GOLD.toLocaleString()} GP</span>
      </div>
      <div class="info-pill">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 14l-5-5 1.41-1.41L12 14.17l7.59-7.59L21 8l-9 9z" />
        </svg>
        <span>Lvl {CHAR.level} {CHAR.cls}</span>
      </div>
    </div>

    <div class="topbar-actions">
      <button
        class="topbar-btn"
        class:active={rulesOpen}
        onclick={() => (rulesOpen = !rulesOpen)}
        aria-pressed={rulesOpen}
      >
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 14H8v-2h8v2zm0-4H8v-2h8v2zm0-4H8V6h8v2z" />
        </svg>
        CONSULT RULES
      </button>
      <button class="topbar-btn primary" onclick={onBattle}>
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M20.57 14.86L22 13.43 20.57 12 17 15.57 8.43 7 12 3.43 10.57 2 9.14 3.43 7.71 2 5.57 4.14 4.14 2.71 2.71 4.14l1.43 1.43L2 7.71l1.43 1.43L2 10.57 3.43 12 7 8.43 15.57 17 12 20.57 13.43 22l1.43-1.43L16.29 22l2.14-2.14-1.43-1.43L19.43 17l-1.43-1.43z" />
        </svg>
        BATTLE MAP
      </button>
    </div>
  </header>

  <!-- ══ BODY (3 columns) ══════════════════════════════════════════════════ -->
  <div class="game-body">

    <!-- ── LEFT SIDEBAR ────────────────────────────────────────────────── -->
    <aside class="left-sidebar">
      <div class="portrait-wrap">
        <div class="portrait-ring">
          <div class="portrait-inner" aria-label="Ritratto personaggio">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
            </svg>
          </div>
          <div class="portrait-badge" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 1L9.5 8.5H2l6 4.5-2.5 7.5L12 16l6.5 4.5-2.5-7.5 6-4.5h-7.5z" />
            </svg>
          </div>
        </div>
        <h2 class="char-name">{CHAR.name}</h2>
        <p class="char-class">LEVEL {CHAR.level} {CHAR.cls.toUpperCase()}</p>
      </div>

      <div class="sidebar-section">
        <span class="section-label">VITALITY</span>
        <div class="vital-row">
          <div class="vital-icon hp-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
            </svg>
          </div>
          <div class="vital-info">
            <div class="vital-header">
              <span class="vital-label">HP</span>
              <span class="vital-value">{CHAR.hp} / {CHAR.maxHp}</span>
            </div>
            <div class="vital-track">
              <div class="vital-fill hp-fill" style="width: {hpPct}%"></div>
            </div>
          </div>
        </div>
        <div class="vital-row">
          <div class="vital-icon mana-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2l2.09 6.43H21l-5.47 3.97 2.09 6.43L12 14.9l-5.62 3.93 2.09-6.43L3 8.43h6.91z" />
            </svg>
          </div>
          <div class="vital-info">
            <div class="vital-header">
              <span class="vital-label">Mana</span>
              <span class="vital-value">{CHAR.mana} / {CHAR.maxMana}</span>
            </div>
            <div class="vital-track">
              <div class="vital-fill mana-fill" style="width: {manaPct}%"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="sidebar-section">
        <span class="section-label">CORE ATTRIBUTES</span>
        <div class="attr-grid">
          {#each CHAR.attrs as attr (attr.key)}
            <div class="attr-card">
              <svg class="attr-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d={attr.icon} />
              </svg>
              <span class="attr-value">{attr.value}</span>
              <span class="attr-key">{attr.key}</span>
            </div>
          {/each}
        </div>
      </div>

      <div class="sidebar-spacer"></div>

      <button class="switch-btn" onclick={onBattle}>
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M20.57 14.86L22 13.43 20.57 12 17 15.57 8.43 7 12 3.43 10.57 2 9.14 3.43 7.71 2 5.57 4.14 4.14 2.71 2.71 4.14l1.43 1.43L2 7.71l1.43 1.43L2 10.57 3.43 12 7 8.43 15.57 17 12 20.57 13.43 22l1.43-1.43L16.29 22l2.14-2.14-1.43-1.43L19.43 17l-1.43-1.43z" />
        </svg>
        SWITCH TO BATTLE MAP
      </button>
    </aside>

    <!-- ── CENTER CHAT ──────────────────────────────────────────────────── -->
    <div class="chat-area">
      <div class="chat-scroll" aria-live="polite" aria-label="Narrazione">
        {#each messages as msg (msg.id)}
          {#if msg.role === 'master'}
            <div class="bubble-row master-row">
              <div class="bubble-avatar master-avatar" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
                </svg>
                <span class="bubble-label">MASTER</span>
              </div>
              <div class="bubble master-bubble">
                <p class="bubble-text">{msg.text}</p>
                {#if msg.note || msg.check}
                  <div class="bubble-footer">
                    {#if msg.note}<span class="bubble-note">{msg.note}</span>{/if}
                    {#if msg.check}<span class="check-badge">{msg.check}</span>{/if}
                  </div>
                {/if}
              </div>
            </div>
          {:else}
            <div class="bubble-row player-row">
              <div class="bubble player-bubble">
                <p class="bubble-text">{msg.text}</p>
              </div>
              <div class="bubble-avatar player-avatar" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
                </svg>
                <span class="bubble-label">YOU</span>
              </div>
            </div>
          {/if}
        {/each}
        <div bind:this={chatEndRef}></div>
      </div>

      <div class="chat-input-bar">
        <input
          class="chat-input"
          type="text"
          bind:value={inputText}
          onkeydown={handleKeydown}
          placeholder="What will you do next, adventurer?"
          aria-label="Descrivi la tua azione"
        />
        <button class="dice-btn" aria-label="Tira dadi">
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M21 6.7C20.9 6.3 20.6 6 20.2 5.9l-8-2.7c-.1 0-.3-.1-.4-.1s-.3 0-.4.1l-8 2.7c-.4.1-.7.4-.8.8L1 7v10.1c0 .4.2.7.5.9l8 4.9c.1.1.3.1.5.1s.4 0 .5-.1l8-4.9c.3-.2.5-.5.5-.9V7c0-.1-.1-.2 0-.3zM11 19.6l-6.5-4v-7.3l6.5 2.2v9.1zm1-10.9L5.8 6.7 12 4.5l6.2 2.2L12 8.7zm7.5 6.9L13 19.6v-9.1l6.5-2.2v7.3z" />
          </svg>
        </button>
        <button class="act-btn" onclick={handleSend} disabled={!inputText.trim()}>
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M8 5v14l11-7z" />
          </svg>
          ACT
        </button>
      </div>
    </div>

    <!-- ── RIGHT PANEL ─────────────────────────────────────────────────── -->
    {#if rulesOpen}
      <RulesConsultant bind:open={rulesOpen} onClose={() => (rulesOpen = false)} />
    {:else}
      <aside class="right-sidebar">
        <!-- EQUIPMENT -->
        <div class="rs-section">
          <button class="rs-heading" onclick={() => (equipOpen = !equipOpen)} aria-expanded={equipOpen}>
            <div class="rs-heading-left">
              <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z" />
              </svg>
              EQUIPMENT
            </div>
            <svg class="chevron" class:rotated={!equipOpen} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z" />
            </svg>
          </button>
          {#if equipOpen}
            <div class="rs-items">
              {#each EQUIPMENT as item (item.id)}
                <div class="equip-row">
                  <div class="equip-icon-wrap">
                    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                      <path d={item.icon} />
                    </svg>
                  </div>
                  <div class="equip-info">
                    <span class="equip-name">{item.name}</span>
                    <span class="equip-slot">{item.slot}</span>
                  </div>
                  <span class="equip-badge {item.badgeColor}">{item.badge}</span>
                </div>
              {/each}
              <button class="show-all">SHOW ALL</button>
            </div>
          {/if}
        </div>

        <!-- ABILITIES -->
        <div class="rs-section">
          <button class="rs-heading" onclick={() => (abilOpen = !abilOpen)} aria-expanded={abilOpen}>
            <div class="rs-heading-left">
              <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M7 2v11h3v9l7-12h-4l4-8z" />
              </svg>
              ABILITIES
            </div>
            <svg class="chevron" class:rotated={!abilOpen} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z" />
            </svg>
          </button>
          {#if abilOpen}
            <div class="rs-items">
              {#each ABILITIES as ab (ab.id)}
                <div class="ability-row">
                  <div class="ability-header">
                    <span class="ability-name">{ab.name}</span>
                    <span class="ability-type {ab.type.toLowerCase()}">{ab.type}</span>
                  </div>
                  <p class="ability-desc">{ab.desc}</p>
                </div>
              {/each}
              <button class="show-all">SHOW ALL</button>
            </div>
          {/if}
        </div>

        <!-- INVENTORY -->
        <div class="rs-section">
          <button class="rs-heading" onclick={() => (invOpen = !invOpen)} aria-expanded={invOpen}>
            <div class="rs-heading-left">
              <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M20 6h-2.18c.07-.44.18-.88.18-1.36C18 2.51 15.49 0 12 0 8.51 0 6 2.51 6 4.64c0 .48.11.92.18 1.36H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-8-4c1.84 0 3 1.16 3 2.64 0 .49-.27.92-.55 1.36h-4.9C9.27 5.56 9 5.13 9 4.64 9 3.16 10.16 2 12 2zm0 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z" />
              </svg>
              INVENTORY
            </div>
            <svg class="chevron" class:rotated={!invOpen} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z" />
            </svg>
          </button>
          {#if invOpen}
            <div class="rs-items">
              <div class="inv-grid">
                {#each INVENTORY_ITEMS as item (item.id)}
                  <div class="inv-slot">
                    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                      <path d={item.icon} />
                    </svg>
                    {#if item.count}<span class="inv-count">{item.count}</span>{/if}
                  </div>
                {/each}
                {#each { length: Math.max(0, 8 - INVENTORY_ITEMS.length) } as _}
                  <div class="inv-slot empty"></div>
                {/each}
              </div>
              <div class="enc-row">
                <span class="enc-label">ENCUMBRANCE</span>
                <span class="enc-value">{ENCUMBRANCE.current} / {ENCUMBRANCE.max} lbs</span>
              </div>
              <div class="enc-track">
                <div class="enc-fill" style="width: {encPct}%"></div>
              </div>
            </div>
          {/if}
        </div>
      </aside>
    {/if}
  </div>

  <!-- ══ STATUS BAR ═════════════════════════════════════════════════════════ -->
  <footer class="status-bar">
    <div class="status-left">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
      </svg>
      <span>DUNGEON OF ETERNAL SHADOWS – LEVEL 4</span>
    </div>
    <div class="status-center">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67V7z" />
      </svg>
      <span>SESSION: 1H 42M</span>
    </div>
    <div class="status-right">
      <span class="ai-dot" aria-hidden="true"></span>
      <span>AI ENGINE ONLINE</span>
    </div>
  </footer>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  :global(.game-screen) {
    --hp-full:  #{$hp-full};
    --hp-mid:   #{$hp-mid};
    --hp-low:   #{$hp-low};
    --mp-color: #{$mp-color};
  }

  .game-screen {
    height: 100vh;
    background: $color-bg-page;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  // ══ TOP BAR ══════════════════════════════════════════════════════════════════
  .game-topbar {
    height: $topbar-height;
    flex-shrink: 0;
    background: $color-bg-page;
    border-bottom: 1px solid $color-border-subtle;
    display: flex;
    align-items: center;
    padding: 0 $space-7;
    gap: $space-6;
    z-index: $z-topbar;
  }

  .logo-wrap {
    display: flex;
    align-items: center;
    gap: $space-3;
    background: none;
    border: none;
    cursor: pointer;
    flex-shrink: 0;
    padding: 0;
    transition: opacity $transition-base;
    &:hover { opacity: 0.80; }
  }

  .logo-icon {
    width: 36px;
    height: 36px;
    background: $color-surface-elevated;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    display: flex;
    align-items: center;
    justify-content: center;
    color: $color-accent;
    svg { width: 20px; height: 20px; }
  }

  .logo-text {
    font-family: $font-sans;
    font-size: 18px;
    font-weight: $font-weight-black;
    color: $color-accent;
    white-space: nowrap;
  }

  .topbar-center {
    flex: 1;
    display: flex;
    justify-content: center;
    gap: $space-3;
  }

  .info-pill {
    display: flex;
    align-items: center;
    gap: $space-2;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: 999px;
    padding: 5px $space-5;
    font-family: $font-sans;
    font-size: $font-size-game-ui;
    font-weight: $font-weight-bold;
    color: $white;
    svg { width: 14px; height: 14px; color: $color-accent; }
  }

  .topbar-actions {
    flex-shrink: 0;
    display: flex;
    gap: $space-3;
  }

  .topbar-btn {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    padding: $space-3 $space-5;
    background: $color-surface;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-game-ui;
    font-weight: $font-weight-bold;
    letter-spacing: 0.5px;
    color: $white;
    white-space: nowrap;
    transition: background $transition-base, border-color $transition-base;
    svg { width: 16px; height: 16px; flex-shrink: 0; }

    &:hover { background: $color-surface-elevated; }

    &.active {
      border-color: $color-accent;
      color: $color-accent;
    }

    &.primary {
      background: $color-btn-primary-bg;
      border-color: $color-btn-primary-bg;
      color: $color-btn-primary-text;
      &:hover { background: $color-btn-primary-hover-bg; box-shadow: $glow-btn-primary; }
    }
  }

  // ══ BODY ═════════════════════════════════════════════════════════════════════
  .game-body {
    flex: 1;
    display: flex;
    overflow: hidden;
  }

  // ── LEFT SIDEBAR ─────────────────────────────────────────────────────────────
  .left-sidebar {
    width: $game-sidebar-width;
    flex-shrink: 0;
    background: $color-surface;
    border-right: 1px solid $color-border-subtle;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    overflow-x: hidden;
    padding: $space-7 $space-6 $space-5;
    gap: $space-5;

    &::-webkit-scrollbar { width: 3px; }
    &::-webkit-scrollbar-thumb { background: $color-border; border-radius: 2px; }
  }

  .portrait-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: $space-2;
  }

  .portrait-ring {
    position: relative;
    width: 88px;
    height: 88px;
  }

  .portrait-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    border: 3px solid $color-accent;
    background: $color-bg-page;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    color: $color-accent;
    svg { width: 48px; height: 48px; }
  }

  .portrait-badge {
    position: absolute;
    bottom: 2px;
    right: 2px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: $color-accent;
    color: $dark-700;
    display: flex;
    align-items: center;
    justify-content: center;
    svg { width: 12px; height: 12px; }
  }

  .char-name {
    font-family: $font-sans;
    font-size: 15px;
    font-weight: $font-weight-black;
    color: $white;
    margin: 0;
    text-align: center;
  }

  .char-class {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-bold;
    letter-spacing: 2px;
    color: $color-accent;
    margin: 0;
    text-align: center;
  }

  .sidebar-section {
    display: flex;
    flex-direction: column;
    gap: $space-3;
  }

  .section-label {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-black;
    letter-spacing: 2px;
    color: $color-text-secondary;
    padding-bottom: $space-1;
    border-bottom: 1px solid $color-border-subtle;
  }

  .vital-row {
    display: flex;
    align-items: center;
    gap: $space-3;
  }

  .vital-icon {
    width: 18px;
    height: 18px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    svg { width: 16px; height: 16px; }
    &.hp-icon   { color: $hp-low; }
    &.mana-icon { color: $mp-color; }
  }

  .vital-info { flex: 1; min-width: 0; }

  .vital-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 4px;
  }

  .vital-label {
    font-family: $font-sans;
    font-size: $font-size-game-stat;
    color: $color-text-secondary;
  }

  .vital-value {
    font-family: $font-sans;
    font-size: $font-size-game-stat;
    font-weight: $font-weight-bold;
    color: $white;
  }

  .vital-track {
    height: 6px;
    background: $color-hp-bg;
    border-radius: 3px;
    overflow: hidden;
  }

  .vital-fill {
    height: 100%;
    border-radius: 3px;
    transition: width 0.4s ease;
    &.hp-fill   { background: $hp-low; }
    &.mana-fill { background: $mp-color; }
  }

  .attr-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: $space-2;
  }

  .attr-card {
    background: $color-bg-page;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-md;
    padding: $space-3 $space-4;
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .attr-icon { width: 14px; height: 14px; color: $color-accent; }

  .attr-value {
    font-family: $font-sans;
    font-size: 18px;
    font-weight: $font-weight-black;
    color: $color-accent;
    line-height: 1;
  }

  .attr-key {
    font-family: $font-sans;
    font-size: 9px;
    font-weight: $font-weight-bold;
    letter-spacing: 1.5px;
    color: $color-text-secondary;
  }

  .sidebar-spacer { flex: 1; }

  .switch-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: $space-3;
    width: 100%;
    padding: $space-4;
    background: $color-btn-primary-bg;
    border: none;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-serif;
    font-size: 13px;
    font-weight: $font-weight-black;
    letter-spacing: 1px;
    color: $color-btn-primary-text;
    flex-shrink: 0;
    transition: $transition-btn;
    svg { width: 16px; height: 16px; }
    &:hover { background: $color-btn-primary-hover-bg; box-shadow: $glow-btn-primary; }
  }

  // ── CENTER CHAT ───────────────────────────────────────────────────────────────
  .chat-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    border-right: 1px solid $color-border-subtle;
    overflow: hidden;
  }

  .chat-scroll {
    flex: 1;
    overflow-y: auto;
    padding: $space-7 $space-8;
    display: flex;
    flex-direction: column;
    gap: $space-6;

    &::-webkit-scrollbar { width: 4px; }
    &::-webkit-scrollbar-thumb { background: $color-border; border-radius: 2px; }
  }

  .bubble-row {
    display: flex;
    align-items: flex-start;
    gap: $space-4;
  }

  .player-row { justify-content: flex-end; }

  .bubble-avatar {
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: $space-1;
  }

  .master-avatar svg,
  .player-avatar svg {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    padding: 6px;
    box-sizing: border-box;
  }

  .master-avatar svg {
    background: $color-surface-elevated;
    color: $color-text-secondary;
  }

  .player-avatar svg {
    background: $color-surface-elevated;
    border: 2px solid $color-accent;
    color: $color-accent;
  }

  .bubble-label {
    font-family: $font-sans;
    font-size: 9px;
    font-weight: $font-weight-black;
    letter-spacing: 1px;
    color: $color-text-secondary;
  }

  .bubble {
    max-width: 70%;
    border-radius: $radius-lg;
    padding: $space-5 $space-6;
  }

  .master-bubble {
    background: $bubble-master-bg;
    border-radius: 0 $radius-lg $radius-lg $radius-lg;
    display: flex;
    flex-direction: column;
    gap: $space-3;
  }

  .player-bubble {
    background: $bubble-player-bg;
    border-radius: $radius-lg $radius-lg 0 $radius-lg;
  }

  .bubble-text {
    font-family: $font-sans;
    font-size: $font-size-game-body;
    line-height: 1.65;
    margin: 0;
    font-style: italic;
    .master-bubble & { color: $bubble-master-text; }
    .player-bubble & { color: $bubble-player-text; font-style: normal; font-weight: $font-weight-semibold; }
  }

  .bubble-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: $space-4;
    padding-top: $space-2;
    border-top: 1px solid rgba($bubble-master-text, 0.12);
  }

  .bubble-note {
    font-family: $font-sans;
    font-size: 12px;
    font-style: italic;
    color: rgba($bubble-master-text, 0.55);
  }

  .check-badge {
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-black;
    letter-spacing: 0.5px;
    color: $mp-color;
    background: rgba($mp-color, 0.14);
    border: 1px solid rgba($mp-color, 0.25);
    border-radius: $radius-sm;
    padding: 3px $space-3;
    white-space: nowrap;
  }

  .chat-input-bar {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: $space-3;
    padding: $space-5 $space-8;
    background: $color-bg-page;
    border-top: 1px solid $color-border-subtle;
  }

  .chat-input {
    flex: 1;
    background: $color-surface;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    padding: $space-4 $space-5;
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-primary;
    transition: border-color $transition-base;
    &::placeholder { color: $color-placeholder; }
    &:focus { outline: none; border-color: $color-border-focus; }
  }

  .dice-btn {
    width: 40px;
    height: 40px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: $color-surface;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    cursor: pointer;
    color: $color-text-secondary;
    transition: $transition-base;
    svg { width: 18px; height: 18px; }
    &:hover { background: $color-surface-elevated; color: $color-accent; }
  }

  .act-btn {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    padding: $space-3 $space-7;
    background: $color-btn-primary-bg;
    border: none;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-serif;
    font-size: 14px;
    font-weight: $font-weight-black;
    letter-spacing: 1px;
    color: $color-btn-primary-text;
    white-space: nowrap;
    transition: $transition-btn;
    svg { width: 16px; height: 16px; }
    &:hover:not(:disabled) { background: $color-btn-primary-hover-bg; box-shadow: $glow-btn-primary; }
    &:disabled { opacity: 0.35; cursor: not-allowed; }
  }

  // ── RIGHT SIDEBAR ─────────────────────────────────────────────────────────────
  .right-sidebar {
    width: $game-sidebar-width;
    flex-shrink: 0;
    background: $color-surface;
    display: flex;
    flex-direction: column;
    overflow-y: auto;

    &::-webkit-scrollbar { width: 3px; }
    &::-webkit-scrollbar-thumb { background: $color-border; border-radius: 2px; }
  }

  .rs-section { border-bottom: 1px solid $color-border-subtle; }

  .rs-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: $space-5 $space-6;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 11px;
    font-weight: $font-weight-black;
    letter-spacing: 2px;
    color: $white;
    text-transform: uppercase;
    &:hover { background: $color-surface-elevated; }
  }

  .rs-heading-left {
    display: flex;
    align-items: center;
    gap: $space-3;
    svg { width: 14px; height: 14px; color: $color-accent; }
  }

  .chevron {
    width: 16px;
    height: 16px;
    color: $color-text-secondary;
    transition: transform $transition-base;
    &.rotated { transform: rotate(-90deg); }
  }

  .rs-items {
    padding: 0 $space-6 $space-5;
    display: flex;
    flex-direction: column;
    gap: $space-3;
  }

  .equip-row {
    display: flex;
    align-items: center;
    gap: $space-3;
  }

  .equip-icon-wrap {
    width: 28px;
    height: 28px;
    background: $color-bg-page;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-sm;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: $color-accent;
    svg { width: 14px; height: 14px; }
  }

  .equip-info {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 1px;
  }

  .equip-name {
    font-family: $font-sans;
    font-size: 12px;
    font-weight: $font-weight-bold;
    color: $white;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .equip-slot {
    font-family: $font-sans;
    font-size: 10px;
    color: $color-text-secondary;
  }

  .equip-badge {
    flex-shrink: 0;
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-bold;
    padding: 2px $space-2;
    border-radius: $radius-sm;
    white-space: nowrap;
    &.green { background: rgba($hp-full, 0.15); color: $hp-full; }
    &.blue  { background: rgba($mp-color, 0.15); color: $mp-color; }
  }

  .ability-row { display: flex; flex-direction: column; gap: 3px; }

  .ability-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: $space-2;
  }

  .ability-name {
    font-family: $font-sans;
    font-size: 12px;
    font-weight: $font-weight-bold;
    color: $white;
  }

  .ability-type {
    font-family: $font-sans;
    font-size: 9px;
    font-weight: $font-weight-black;
    letter-spacing: 0.5px;
    padding: 2px $space-2;
    border-radius: $radius-sm;
    &.passive { background: rgba($color-text-secondary, 0.2); color: $color-text-secondary; }
    &.combat  { background: rgba($red-400, 0.15); color: $red-400; }
  }

  .ability-desc {
    font-family: $font-sans;
    font-size: 11px;
    color: $color-text-secondary;
    margin: 0;
    line-height: 1.4;
  }

  .show-all {
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 10px;
    font-weight: $font-weight-black;
    letter-spacing: 1px;
    color: $color-accent;
    padding: $space-1 0;
    align-self: center;
    transition: opacity $transition-base;
    &:hover { opacity: 0.7; }
  }

  .inv-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: $space-2;
  }

  .inv-slot {
    position: relative;
    aspect-ratio: 1;
    background: $color-bg-page;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-sm;
    display: flex;
    align-items: center;
    justify-content: center;
    color: $color-accent;
    svg { width: 16px; height: 16px; }
    &.empty { border-style: dashed; }
  }

  .inv-count {
    position: absolute;
    bottom: 2px;
    right: 3px;
    font-family: $font-sans;
    font-size: 9px;
    font-weight: $font-weight-bold;
    color: $color-accent;
    line-height: 1;
  }

  .enc-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .enc-label {
    font-family: $font-sans;
    font-size: 9px;
    font-weight: $font-weight-black;
    letter-spacing: 1.5px;
    color: $color-text-secondary;
  }

  .enc-value {
    font-family: $font-sans;
    font-size: 10px;
    color: $color-text-secondary;
  }

  .enc-track {
    height: 5px;
    background: $color-hp-bg;
    border-radius: 3px;
    overflow: hidden;
  }

  .enc-fill {
    height: 100%;
    background: $hp-mid;
    border-radius: 3px;
    transition: width 0.4s ease;
  }

  // ══ STATUS BAR ═══════════════════════════════════════════════════════════════
  .status-bar {
    flex-shrink: 0;
    height: 32px;
    background: $color-bg;
    border-top: 1px solid $color-border-subtle;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 $space-7;
    gap: $space-6;

    svg { width: 12px; height: 12px; color: $color-accent; }
  }

  .status-left  { display: flex; align-items: center; gap: $space-2; font-family: $font-sans; font-size: 10px; font-weight: $font-weight-semibold; letter-spacing: 0.5px; color: $color-text-secondary; }
  .status-center { display: flex; align-items: center; gap: $space-2; font-family: $font-sans; font-size: 10px; font-weight: $font-weight-semibold; letter-spacing: 0.5px; color: $color-text-secondary; }
  .status-right  { display: flex; align-items: center; gap: $space-2; font-family: $font-sans; font-size: 10px; font-weight: $font-weight-semibold; letter-spacing: 0.5px; color: $color-text-secondary; }

  .ai-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: $hp-full;
    flex-shrink: 0;
  }
</style>
