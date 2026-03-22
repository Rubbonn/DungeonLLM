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
      <button class="btn btn-primary">
        <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"
          />
        </svg>
        NUOVA CAMPAGNA
      </button>

      <!-- Load campaign -->
      <button class="btn btn-secondary">
        <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M20 6h-8l-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2z"
          />
        </svg>
        CARICA CAMPAGNA
      </button>

      <!-- Create campaign -->
      <button class="btn btn-secondary">
        <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path
            d="M7.5 5.6L10 7 8.6 4.5 10 2 7.5 3.4 5 2l1.4 2.5L5 7zm12 9.8L17 14l1.4 2.5L17 19l2.5-1.4L22 19l-1.4-2.5L22 14zM22 2l-2.5 1.4L17 2l1.4 2.5L17 7l2.5-1.4L22 7l-1.4-2.5zm-7.63 5.29a1.5 1.5 0 00-2.12 0L3 16.54V21h4.46l9.25-9.25a1.5 1.5 0 000-2.12l-2.34-2.34z"
          />
        </svg>
        CREA CAMPAGNA
      </button>
    </nav>

    <!-- Settings link -->
    <button class="settings-btn">
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

<style>
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
    background-color: #060402;
  }

  /* ── Atmospheric dungeon background ── */
  .bg-overlay {
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse 80% 100% at 8% 50%, rgba(5, 3, 1, 0.97) 0%, transparent 58%),
      radial-gradient(ellipse 80% 100% at 92% 50%, rgba(5, 3, 1, 0.97) 0%, transparent 58%),
      radial-gradient(ellipse 40% 80% at 50% 0%, rgba(8, 6, 3, 0.92) 0%, transparent 80%),
      radial-gradient(ellipse 38% 65% at 50% 50%, rgba(28, 17, 6, 0.55) 0%, transparent 100%),
      linear-gradient(180deg, #060402 0%, #110e07 35%, #0a0805 65%, #060402 100%);
    z-index: 0;
  }

  /* ── Orange portal / dungeon-door glow ── */
  .portal-glow {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -8%);
    width: 380px;
    height: 240px;
    background: radial-gradient(
      ellipse 62% 100% at 50% 100%,
      rgba(255, 125, 15, 0.88) 0%,
      rgba(218, 82, 8, 0.55) 28%,
      rgba(155, 48, 4, 0.22) 55%,
      transparent 72%
    );
    z-index: 1;
    filter: blur(12px);
    pointer-events: none;
  }

  /* ── Main content ── */
  .main-content {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 520px;
    padding: 0 24px;
    margin-top: -30px;
  }

  /* ── Header ── */
  .header {
    text-align: center;
    margin-bottom: 48px;
  }

  .shield-icon {
    width: 46px;
    height: 46px;
    margin: 0 auto 14px;
    color: #f5c518;
    filter: drop-shadow(0 0 12px rgba(245, 197, 24, 0.72));
  }

  .shield-icon svg {
    width: 100%;
    height: 100%;
  }

  .title {
    font-family: 'Cinzel', Georgia, 'Times New Roman', serif;
    font-size: clamp(52px, 9.5vw, 96px);
    font-weight: 900;
    color: #f5c518;
    letter-spacing: 5px;
    line-height: 1;
    margin: 0 0 14px;
    text-shadow:
      0 0 40px rgba(245, 197, 24, 0.28),
      0 2px 6px rgba(0, 0, 0, 0.95);
  }

  .subtitle {
    font-family: 'Cinzel', Georgia, serif;
    font-size: 12px;
    letter-spacing: 8px;
    color: #8a7a58;
    text-transform: uppercase;
    font-weight: 400;
    margin: 0;
  }

  /* ── Menu buttons ── */
  .menu {
    display: flex;
    flex-direction: column;
    gap: 12px;
    width: 100%;
    max-width: 420px;
    margin-bottom: 28px;
  }

  .btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 17px 28px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-family: 'Cinzel', Georgia, serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    transition:
      transform 0.15s ease,
      box-shadow 0.15s ease,
      background-color 0.15s ease;
    width: 100%;
  }

  .btn:active {
    transform: translateY(1px) !important;
  }

  .btn-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
  }

  .btn-primary {
    background: #f5c518;
    color: #1a1108;
  }

  .btn-primary:hover {
    background: #ffd900;
    box-shadow: 0 0 28px rgba(245, 197, 24, 0.55);
    transform: translateY(-2px);
  }

  .btn-secondary {
    background: rgba(40, 24, 10, 0.9);
    color: #f5c518;
    border: 1px solid rgba(245, 197, 24, 0.07);
  }

  .btn-secondary:hover {
    background: rgba(58, 34, 13, 0.95);
    border-color: rgba(245, 197, 24, 0.22);
    transform: translateY(-2px);
  }

  /* ── Settings link ── */
  .settings-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    background: none;
    border: none;
    cursor: pointer;
    font-family: 'Cinzel', Georgia, serif;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 3px;
    color: #f5c518;
    padding: 10px 16px;
    opacity: 0.82;
    transition: opacity 0.2s;
  }

  .settings-btn:hover {
    opacity: 1;
  }

  .settings-btn .btn-icon {
    width: 16px;
    height: 16px;
  }

  /* ── Footer ── */
  .footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 20px 22px;
    pointer-events: none;
  }

  .footer-nav {
    display: flex;
    gap: 44px;
    margin-bottom: 10px;
    pointer-events: auto;
  }

  .footer-link {
    display: flex;
    align-items: center;
    gap: 6px;
    background: none;
    border: none;
    cursor: pointer;
    font-family: 'Cinzel', Georgia, serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    color: #7a6a4a;
    padding: 4px 8px;
    transition: color 0.2s;
  }

  .footer-link:hover {
    color: #f5c518;
  }

  .nav-icon {
    width: 14px;
    height: 14px;
  }

  .version {
    font-family: 'Cinzel', Georgia, serif;
    font-size: 10px;
    letter-spacing: 3px;
    color: #5a4a2a;
    opacity: 0.65;
    margin: 0;
  }
</style>
