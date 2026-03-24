<script>
  import CharacterCreation from './pages/CharacterCreation.svelte';
  import LoadCampaign from './pages/LoadCampaign.svelte';
  import NewCampaign from './pages/NewCampaign.svelte';
  import GameScreen from './pages/GameScreen.svelte';
  import BattleView from './pages/BattleView.svelte';
  import SettingsModal from './components/SettingsModal.svelte';

  let currentPage    = $state('home');
  let showSettings   = $state(false);
  let activeCampaign = $state(null);

  function startCampaign(campaign) {
    activeCampaign = campaign;
    currentPage = 'game';
  }
</script>

{#if currentPage === 'character-creation'}
  <CharacterCreation onBack={() => (currentPage = 'home')} />
{:else if currentPage === 'load-campaign'}
  <LoadCampaign
    onBack={() => (currentPage = 'home')}
    onPlay={(c) => startCampaign(c)}
  />
{:else if currentPage === 'new-campaign'}
  <NewCampaign
    onBack={() => (currentPage = 'home')}
    onStart={(module) => startCampaign(module)}
  />
{:else if currentPage === 'game'}
  <GameScreen
    campaign={activeCampaign}
    onBack={() => (currentPage = 'home')}
    onBattle={() => (currentPage = 'battle')}
  />
{:else if currentPage === 'battle'}
  <BattleView
    campaign={activeCampaign}
    onBack={() => (currentPage = 'game')}
  />
{:else}
<div class="dungeon-app">
  <!-- Atmospheric background layers -->
  <div class="bg-overlay" aria-hidden="true"></div>
  <!-- Portal / dungeon-door glow -->
  <div class="portal-glow" aria-hidden="true"></div>

  <!-- Main content -->
  <main class="main-content">
    <header class="header">
      <!-- Shield icon -->
      <div class="shield-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z" />
        </svg>
      </div>

      <h1 class="title">DUNGEONLLM</h1>
      <p class="subtitle">THE AI MASTER'S DOMAIN</p>
    </header>

    <nav class="menu" aria-label="Navigazione principale">
      <!-- New campaign -->
      <button class="btn btn-primary" onclick={() => (currentPage = 'new-campaign')}>
        <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"
          />
        </svg>
        NUOVA CAMPAGNA
      </button>

      <!-- Load campaign -->
      <button class="btn btn-secondary" onclick={() => (currentPage = 'load-campaign')}>
        <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M20 6h-8l-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2z"
          />
        </svg>
        CARICA CAMPAGNA
      </button>

      <!-- Create campaign -->
      <button class="btn btn-secondary" onclick={() => (currentPage = 'character-creation')}>
        <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M7.5 5.6L10 7 8.6 4.5 10 2 7.5 3.4 5 2l1.4 2.5L5 7zm12 9.8L17 14l1.4 2.5L17 19l2.5-1.4L22 19l-1.4-2.5L22 14zM22 2l-2.5 1.4L17 2l1.4 2.5L17 7l2.5-1.4L22 7l-1.4-2.5zm-7.63 5.29a1.5 1.5 0 00-2.12 0L3 16.54V21h4.46l9.25-9.25a1.5 1.5 0 000-2.12l-2.34-2.34z"
          />
        </svg>
        CREA CAMPAGNA
      </button>
    </nav>

    <!-- Settings link -->
    <button class="settings-btn" onclick={() => (showSettings = true)}>
      <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path
          d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32a.49.49 0 0 0-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54a.484.484 0 0 0-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96a.465.465 0 0 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"
        />
      </svg>
      IMPOSTAZIONI
    </button>
  </main>

  <!-- Footer -->
  <footer class="footer">
    <nav class="footer-nav" aria-label="Navigazione secondaria">
      <button class="footer-link">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M4 6H2v14c0 1.1.9 2 2 2h14v-2H4V6zm16-4H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-1 9H9V9h10v2zm-4 4H9v-2h6v2zm4-8H9V5h10v2z"
          />
        </svg>
        LIBRARY
      </button>

      <button class="footer-link">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M9.5 11L3 17.5V21h3.5L13 14.5 9.5 11zm8.84-7.84l-2.5-2.5c-.78-.78-2.05-.78-2.83 0l-2.38 2.38c-.78.78-.78 2.05 0 2.83l2.5 2.5c.78.78 2.05.78 2.83 0l2.38-2.38c.78-.78.78-2.05 0-2.83z"
          />
        </svg>
        FORGE
      </button>
    </nav>

    <p class="version">V0.0.4 BETA PHASE</p>
  </footer>
</div>
{/if}

<!-- Settings modal (rendered over home) -->
<SettingsModal
  open={showSettings}
  onClose={() => (showSettings = false)}
  onSave={() => (showSettings = false)}
/>

<style lang="scss">
  @use './styles/variables' as *;

  .dungeon-app {
    position: relative;
    width: 100%;
    min-height: 100vh;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background-color: $color-bg;
  }

  // ── Atmospheric dungeon background ──────────────────────────────────────────
  .bg-overlay {
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse 80% 100% at 8%  50%, $overlay-strong 0%, transparent 58%),
      radial-gradient(ellipse 80% 100% at 92% 50%, $overlay-strong 0%, transparent 58%),
      radial-gradient(ellipse 40%  80% at 50%  0%, $overlay-warm   0%, transparent 80%),
      radial-gradient(ellipse 38%  65% at 50% 50%, $overlay-center 0%, transparent 100%),
      linear-gradient(180deg, $color-bg 0%, $color-bg-mid 35%, $color-bg-deep 65%, $color-bg 100%);
    z-index: $z-bg;
  }

  // ── Orange portal / dungeon-door glow ───────────────────────────────────────
  .portal-glow {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -8%);
    width: $portal-width;
    height: $portal-height;
    background: radial-gradient(
      ellipse 62% 100% at 50% 100%,
      $portal-core  0%,
      $portal-mid   28%,
      $portal-outer 55%,
      transparent   72%
    );
    z-index: $z-portal;
    filter: blur(12px);
    pointer-events: none;
  }

  // ── Main content ────────────────────────────────────────────────────────────
  .main-content {
    position: relative;
    z-index: $z-content;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: $content-max-width;
    padding: 0 $space-9;
    margin-top: -30px;
  }

  // ── Header ──────────────────────────────────────────────────────────────────
  .header {
    text-align: center;
    margin-bottom: $space-12;
  }

  .shield-icon {
    width: $shield-size;
    height: $shield-size;
    margin: 0 auto $space-5;
    color: $color-icon;
    filter: drop-shadow($glow-shield);

    svg {
      width: 100%;
      height: 100%;
    }
  }

  .title {
    font-family: $font-display;
    font-size: $font-size-title;
    font-weight: $font-weight-black;
    color: $color-accent;
    letter-spacing: $letter-spacing-title;
    line-height: 1;
    margin: 0 0 $space-5;
    text-shadow: $glow-title;
  }

  .subtitle {
    font-family: $font-serif;
    font-size: $font-size-subtitle;
    letter-spacing: $letter-spacing-subtitle;
    color: $color-text-muted;
    text-transform: uppercase;
    font-weight: $font-weight-regular;
    margin: 0;
  }

  // ── Menu buttons ────────────────────────────────────────────────────────────
  .menu {
    display: flex;
    flex-direction: column;
    gap: $space-4;
    width: 100%;
    max-width: $menu-max-width;
    margin-bottom: $space-10;
  }

  .btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: $space-4;
    padding: 17px $space-10;
    border-radius: $radius-md;
    border: none;
    cursor: pointer;
    font-family: $font-serif;
    font-size: $font-size-btn;
    font-weight: $font-weight-bold;
    letter-spacing: $letter-spacing-btn;
    transition: $transition-btn;
    width: 100%;

    &:active {
      transform: translateY(1px) !important;
    }

    // ── Primary (gold fill) ──
    &-primary {
      background: $color-btn-primary-bg;
      color: $color-btn-primary-text;

      &:hover {
        background: $color-btn-primary-hover-bg;
        box-shadow: $glow-btn-primary;
        transform: translateY(-2px);
      }
    }

    // ── Secondary (dark, gold text) ──
    &-secondary {
      background: $color-btn-secondary-bg;
      color: $color-btn-secondary-text;
      border: 1px solid $color-btn-secondary-border;

      &:hover {
        background: $color-btn-secondary-hover-bg;
        border-color: $color-btn-secondary-border-hover;
        transform: translateY(-2px);
      }
    }
  }

  .btn-icon {
    width: $btn-icon-size;
    height: $btn-icon-size;
    flex-shrink: 0;
  }

  // ── Settings link ───────────────────────────────────────────────────────────
  .settings-btn {
    display: flex;
    align-items: center;
    gap: $space-2;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-serif;
    font-size: $font-size-settings;
    font-weight: $font-weight-semibold;
    letter-spacing: $letter-spacing-btn;
    color: $color-text-accent;
    padding: $space-3 $space-6;
    opacity: 0.82;
    transition: opacity $transition-base;

    &:hover {
      opacity: 1;
    }

    .btn-icon {
      width: $settings-icon-size;
      height: $settings-icon-size;
    }
  }

  // ── Footer ──────────────────────────────────────────────────────────────────
  .footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: $z-content;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 $space-7 $space-8;
    pointer-events: none;
  }

  .footer-nav {
    display: flex;
    gap: $space-11;
    margin-bottom: $space-3;
    pointer-events: auto;
  }

  .footer-link {
    display: flex;
    align-items: center;
    gap: $space-1 + 2px;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-serif;
    font-size: $font-size-nav;
    font-weight: $font-weight-semibold;
    letter-spacing: $letter-spacing-nav;
    color: $color-text-dim;
    padding: $space-1 $space-2;
    transition: color $transition-base;

    &:hover {
      color: $color-accent;
    }
  }

  .nav-icon {
    width: $nav-icon-size;
    height: $nav-icon-size;
  }

  .version {
    font-family: $font-serif;
    font-size: $font-size-version;
    letter-spacing: $letter-spacing-version;
    color: $color-text-faint;
    opacity: 0.65;
    margin: 0;
  }
</style>
