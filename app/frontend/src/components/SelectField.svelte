<script>
  /**
   * label   — uppercase label shown inside the control (e.g. "RAZZA")
   * options — string[] or { value, label }[]
   * value   — bound selected value
   */
  let { label, options = [], value = $bindable('') } = $props();

  function optionValue(opt) {
    return typeof opt === 'string' ? opt : opt.value;
  }
  function optionLabel(opt) {
    return typeof opt === 'string' ? opt : opt.label;
  }
</script>

<div class="select-field">
  <span class="select-label">{label}</span>

  <div class="select-wrapper">
    <select class="select-native" bind:value>
      {#each options as opt}
        <option value={optionValue(opt)}>{optionLabel(opt)}</option>
      {/each}
    </select>

    <!-- Chevron -->
    <svg
      class="chevron"
      viewBox="0 0 24 24"
      fill="currentColor"
      aria-hidden="true"
    >
      <path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z" />
    </svg>
  </div>
</div>

<style lang="scss">
  @use '../styles/variables' as *;

  .select-field {
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-md;
    padding: $space-3 $space-6 $space-4;
    cursor: pointer;
    transition: border-color $transition-base;

    &:focus-within {
      border-color: $color-border-focus;
    }
  }

  .select-label {
    display: block;
    font-family: $font-serif;
    font-size: $font-size-field-label;
    font-weight: $font-weight-bold;
    letter-spacing: $letter-spacing-label;
    text-transform: uppercase;
    color: $color-accent;
    margin-bottom: $space-1;
  }

  .select-wrapper {
    position: relative;
    display: flex;
    align-items: center;
  }

  .select-native {
    width: 100%;
    background: none;
    border: none;
    outline: none;
    appearance: none;
    font-family: $font-sans;
    font-size: 17px;
    font-weight: $font-weight-semibold;
    color: $color-text-primary;
    cursor: pointer;
    padding-right: $space-9;

    option {
      background: $olive-900;
      color: $cream;
    }
  }

  .chevron {
    position: absolute;
    right: 0;
    width: 20px;
    height: 20px;
    color: $color-accent-muted;
    pointer-events: none;
    flex-shrink: 0;
  }
</style>
