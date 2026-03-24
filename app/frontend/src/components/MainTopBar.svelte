<script>
  /** onSettings — called when the gear icon is clicked (optional) */
  let { onSettings } = $props();
</script>

<header class="main-topbar">
  <!-- Brand -->
  <div class="brand">
    <!-- Castle / tower icon -->
    <svg class="brand-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M9 3H7v2H5V3H3v6h2v11h14V9h2V3h-2v2h-2V3h-2v2h-2V3H9zm7 16H8V9h8v10z" />
    </svg>
    <span class="brand-name">DungeonLLM</span>
  </div>

  <!-- Actions -->
  <div class="actions">
    <button class="icon-btn" onclick={onSettings} aria-label="Impostazioni">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path
          d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32a.49.49 0 0 0-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54A.484.484 0 0 0 14 3h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96a.465.465 0 0 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"
        />
      </svg>
    </button>

    <button class="avatar-btn" aria-label="Profilo utente">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
      </svg>
    </button>
  </div>
</header>

<style lang="scss">
  @use '../styles/variables' as *;

  .main-topbar {
    position: sticky;
    top: 0;
    left: 0;
    right: 0;
    height: $topbar-height;
    background: $color-bg-page;
    border-bottom: 1px solid $color-border-subtle;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 $space-9;
    z-index: $z-topbar;
  }

  // ── Brand ───────────────────────────────────────────────────────────────────
  .brand {
    display: flex;
    align-items: center;
    gap: $space-3;
  }

  .brand-icon {
    width: 26px;
    height: 26px;
    color: $color-accent;
  }

  .brand-name {
    font-family: $font-sans;
    font-size: 17px;
    font-weight: $font-weight-bold;
    color: $color-text-primary;
    letter-spacing: 0.2px;
  }

  // ── Actions ─────────────────────────────────────────────────────────────────
  .actions {
    display: flex;
    align-items: center;
    gap: $space-3;
  }

  .icon-btn {
    width: $avatar-size;
    height: $avatar-size;
    border-radius: $radius-md;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: $color-accent;
    transition: background $transition-base, border-color $transition-base;

    svg {
      width: 18px;
      height: 18px;
    }

    &:hover {
      background: $color-surface-elevated;
      border-color: $color-border;
    }
  }

  .avatar-btn {
    width: $avatar-size;
    height: $avatar-size;
    border-radius: 50%;
    background: $color-surface;
    border: 1px solid $color-border;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: $color-accent;
    transition: border-color $transition-base, background $transition-base;

    svg {
      width: 20px;
      height: 20px;
    }

    &:hover {
      border-color: $color-border-focus;
      background: $color-surface-elevated;
    }
  }
</style>
