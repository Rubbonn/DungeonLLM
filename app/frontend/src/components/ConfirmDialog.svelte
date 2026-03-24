<script>
  /**
   * Generic confirmation / destructive-action dialog.
   *
   * open          — controls visibility
   * title         — dialog heading
   * body          — main descriptive text
   * bodyNote      — secondary italic note below body (optional)
   * confirmText   — label for the confirm button (default "Conferma")
   * cancelText    — label for the cancel button  (default "Annulla")
   * variant       — 'danger' (red confirm btn) | 'warning' | 'info' (default 'danger')
   * onConfirm     — callback fired on confirm
   * onCancel      — callback fired on cancel / backdrop click
   */
  let {
    open = false,
    title,
    body,
    bodyNote = '',
    confirmText = 'Conferma',
    cancelText  = 'Annulla',
    variant     = 'danger',
    onConfirm,
    onCancel,
  } = $props();

  function handleBackdrop(e) {
    if (e.target === e.currentTarget) onCancel?.();
  }

  function handleKeydown(e) {
    if (e.key === 'Escape') onCancel?.();
  }
</script>

{#if open}
  <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
  <div
    class="backdrop"
    role="dialog"
    aria-modal="true"
    aria-labelledby="dialog-title"
    tabindex="-1"
    onmousedown={handleBackdrop}
    onkeydown={handleKeydown}
  >
    <div class="dialog">
      <!-- Icon -->
      <div class="dialog-icon" class:danger={variant === 'danger'} class:warning={variant === 'warning'} class:info={variant === 'info'} aria-hidden="true">
        {#if variant === 'danger' || variant === 'warning'}
          <!-- Warning triangle -->
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z" />
          </svg>
        {:else}
          <!-- Info circle -->
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z" />
          </svg>
        {/if}
      </div>

      <!-- Heading -->
      <h2 class="dialog-title" id="dialog-title">{title}</h2>

      <!-- Body -->
      <p class="dialog-body">{body}</p>
      {#if bodyNote}
        <p class="dialog-note">{bodyNote}</p>
      {/if}

      <!-- Actions -->
      <div class="dialog-actions">
        <button class="btn-cancel" onclick={onCancel}>{cancelText}</button>
        <button
          class="btn-confirm"
          class:danger={variant === 'danger'}
          class:warning={variant === 'warning'}
          onclick={onConfirm}
        >{confirmText}</button>
      </div>
    </div>
  </div>
{/if}

<style lang="scss">
  @use '../styles/variables' as *;

  // ── Backdrop ─────────────────────────────────────────────────────────────────
  .backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(3px);
    -webkit-backdrop-filter: blur(3px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: $z-modal;
    padding: $space-9;
  }

  // ── Dialog card ──────────────────────────────────────────────────────────────
  .dialog {
    background: $color-surface;
    border: 1px solid $color-border;
    border-radius: $radius-lg;
    padding: $space-9 $space-10 $space-10;
    width: 100%;
    max-width: 420px;
    display: flex;
    flex-direction: column;
    gap: $space-5;
  }

  // ── Icon circle ──────────────────────────────────────────────────────────────
  .dialog-icon {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;

    svg {
      width: 26px;
      height: 26px;
    }

    &.danger, &.warning {
      background: $color-danger-icon-bg;
      color: $color-danger-icon;
    }

    &.info {
      background: rgba($gold-500, 0.14);
      color: $color-accent;
    }
  }

  // ── Text ─────────────────────────────────────────────────────────────────────
  .dialog-title {
    font-family: $font-sans;
    font-size: 20px;
    font-weight: $font-weight-bold;
    color: $white;
    margin: 0;
    line-height: 1.2;
  }

  .dialog-body {
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-primary;
    margin: 0;
    line-height: 1.55;
  }

  .dialog-note {
    font-family: $font-sans;
    font-size: $font-size-caption;
    font-style: italic;
    color: $color-text-secondary;
    margin: 0;
    line-height: 1.5;
  }

  // ── Action buttons ───────────────────────────────────────────────────────────
  .dialog-actions {
    display: flex;
    justify-content: flex-end;
    gap: $space-3;
    margin-top: $space-3;
  }

  .btn-cancel {
    padding: $space-3 $space-7;
    background: $color-surface-elevated;
    border: 1px solid $color-border;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-body;
    font-weight: $font-weight-semibold;
    color: $color-text-primary;
    transition: background $transition-base, border-color $transition-base;

    &:hover {
      background: $color-border;
      border-color: $color-border-focus;
    }
  }

  .btn-confirm {
    padding: $space-3 $space-7;
    border: none;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-body;
    font-weight: $font-weight-bold;
    color: $white;
    transition: background $transition-base, box-shadow $transition-base;

    &.danger, &.warning {
      background: $color-btn-danger-bg;

      &:hover {
        background: $color-btn-danger-hover-bg;
        box-shadow: 0 0 20px rgba($red-500, 0.40);
      }
    }

    &:not(.danger):not(.warning) {
      background: $color-btn-primary-bg;
      color: $color-btn-primary-text;

      &:hover {
        background: $color-btn-primary-hover-bg;
        box-shadow: $glow-btn-primary;
      }
    }

    &:active {
      transform: translateY(1px);
    }
  }
</style>
