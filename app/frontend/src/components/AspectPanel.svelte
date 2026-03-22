<script>
  /** imageUrl — optional portrait URL; shows a placeholder when empty */
  let { imageUrl = '' } = $props();
</script>

<div class="aspect-panel">
  <div class="portrait-frame">
    {#if imageUrl}
      <img class="portrait-img" src={imageUrl} alt="Aspetto del personaggio" />
    {:else}
      <!-- Atmospheric placeholder -->
      <div class="portrait-placeholder" aria-hidden="true">
        <svg class="placeholder-icon" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 12c2.7 0 5-2.3 5-5s-2.3-5-5-5-5 2.3-5 5 2.3 5 5 5zm0 2c-3.33 0-10 1.67-10 5v2h20v-2c0-3.33-6.67-5-10-5z" />
        </svg>
      </div>
    {/if}
  </div>

  <p class="portrait-caption">Il volto di chi sfida l'ignoto</p>

  <button class="btn-generate">
    <svg class="generate-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z" />
      <path d="M7 2l1 3-3-1 3 1-1 3 1-3 3 1-3-1 1-3-1 3-3-1z" opacity="0.6" />
    </svg>
    GENERA CON IA
  </button>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  .aspect-panel {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: $space-4;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-lg;
    padding: $space-6;
    height: 100%;
  }

  // ── Portrait frame ───────────────────────────────────────────────────────────
  .portrait-frame {
    width: 100%;
    aspect-ratio: 4 / 5;
    border-radius: $radius-md;
    overflow: hidden;
    background: $color-bg-page;
    border: 1px solid $color-border;
    flex-shrink: 0;
  }

  .portrait-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  .portrait-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(
      ellipse 70% 80% at 50% 60%,
      rgba(245, 197, 24, 0.07) 0%,
      transparent 70%
    );
  }

  .placeholder-icon {
    width: 72px;
    height: 72px;
    color: rgba($gold-500, 0.18);
  }

  // ── Caption ──────────────────────────────────────────────────────────────────
  .portrait-caption {
    font-family: $font-sans;
    font-size: $font-size-caption;
    font-style: italic;
    color: $color-text-secondary;
    text-align: center;
    margin: 0;
  }

  // ── Generate button ──────────────────────────────────────────────────────────
  .btn-generate {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: $space-2;
    width: 100%;
    padding: $space-4 $space-9;
    background: $color-surface-elevated;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-serif;
    font-size: $font-size-btn;
    font-weight: $font-weight-bold;
    letter-spacing: $letter-spacing-btn;
    color: $color-accent;
    transition: background $transition-base, border-color $transition-base;

    &:hover {
      background: rgba($olive-800, 0.8);
      border-color: $color-border-focus;
    }

    &:active {
      transform: translateY(1px);
    }
  }

  .generate-icon {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
  }
</style>
