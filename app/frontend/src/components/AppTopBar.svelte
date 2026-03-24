<script lang="ts">
  interface Props {
    onBack: () => void;
  }

  let { onBack }: Props = $props();
</script>

<header class="topbar">
  <!-- Brand -->
  <div class="topbar-brand">
    <svg class="brand-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M12 2l2.09 6.43H21l-5.47 3.97 2.09 6.43L12 14.9l-5.62 3.93 2.09-6.43L3 8.43h6.91z" />
    </svg>
    <span class="brand-name">DUNGEONLLM</span>
  </div>

  <!-- Actions -->
  <div class="topbar-actions">
    <button class="back-btn" onclick={onBack} aria-label="Torna indietro">
      <svg class="back-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
      </svg>
      Indietro
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

  .topbar {
    position: fixed;
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
  .topbar-brand {
    display: flex;
    align-items: center;
    gap: $space-2;
  }

  .brand-icon {
    width: 22px;
    height: 22px;
    color: $color-accent;
  }

  .brand-name {
    font-family: $font-serif;
    font-size: 15px;
    font-weight: $font-weight-bold;
    letter-spacing: $letter-spacing-btn;
    color: $color-accent;
  }

  // ── Actions ─────────────────────────────────────────────────────────────────
  .topbar-actions {
    display: flex;
    align-items: center;
    gap: $space-4;
  }

  .back-btn {
    display: flex;
    align-items: center;
    gap: $space-1;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-secondary;
    padding: $space-2 $space-4;
    border-radius: $radius-md;
    transition: color $transition-base;

    &:hover {
      color: $color-text-primary;
    }
  }

  .back-icon {
    width: 18px;
    height: 18px;
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
