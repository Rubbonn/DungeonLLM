<script>
  /**
   * label         — attribute name shown in uppercase (e.g. "FORZA")
   * value         — current numeric value
   * canIncrement  — whether the + button should be enabled
   * canDecrement  — whether the − button should be enabled
   * onIncrement   — callback fired when + is clicked
   * onDecrement   — callback fired when − is clicked
   */
  let { label, value, canIncrement = true, canDecrement = true, onIncrement, onDecrement } = $props();
</script>

<div class="attr-card">
  <div class="attr-header">
    <span class="attr-label">{label}</span>
    <span class="attr-value">{value}</span>
  </div>

  <div class="attr-controls">
    <button
      class="ctrl-btn"
      onclick={onDecrement}
      disabled={!canDecrement}
      aria-label="Diminuisci {label}"
    >−</button>

    <button
      class="ctrl-btn"
      onclick={onIncrement}
      disabled={!canIncrement}
      aria-label="Aumenta {label}"
    >+</button>
  </div>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  .attr-card {
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-md;
    padding: $space-5 $space-6 $space-5;
    display: flex;
    flex-direction: column;
    gap: $space-4;
  }

  // ── Header row: label + value ────────────────────────────────────────────────
  .attr-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .attr-label {
    font-family: $font-serif;
    font-size: $font-size-field-label;
    font-weight: $font-weight-bold;
    letter-spacing: $letter-spacing-label;
    text-transform: uppercase;
    color: $color-text-secondary;
  }

  .attr-value {
    font-family: $font-serif;
    font-size: $font-size-attr-value;
    font-weight: $font-weight-black;
    color: $color-accent;
    line-height: 1;
  }

  // ── Controls row: − and + ────────────────────────────────────────────────────
  .attr-controls {
    display: flex;
    gap: $space-3;
  }

  .ctrl-btn {
    flex: 1;
    padding: $space-3 0;
    background: $color-surface-elevated;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-sm;
    cursor: pointer;
    font-family: $font-sans;
    font-size: 18px;
    font-weight: $font-weight-bold;
    color: $color-text-primary;
    line-height: 1;
    transition: background $transition-fast, border-color $transition-fast, color $transition-fast;

    &:hover:not(:disabled) {
      background: $color-border;
      border-color: $color-border;
      color: $color-accent;
    }

    &:active:not(:disabled) {
      transform: translateY(1px);
    }

    &:disabled {
      opacity: 0.28;
      cursor: not-allowed;
    }
  }
</style>
