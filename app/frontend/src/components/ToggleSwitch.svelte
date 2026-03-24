<script>
  /**
   * checked  — current ON/OFF state (bindable)
   * onToggle — optional callback called with the new boolean value
   * label    — accessible aria-label for the button
   */
  let { checked = $bindable(false), onToggle, label = 'Toggle' } = $props();

  function handleClick() {
    checked = !checked;
    onToggle?.(checked);
  }
</script>

<button
  class="toggle"
  class:on={checked}
  role="switch"
  aria-checked={checked}
  aria-label={label}
  onclick={handleClick}
  type="button"
>
  <span class="thumb"></span>
</button>

<style lang="scss">
  @use '../styles/variables' as *;

  .toggle {
    position: relative;
    display: inline-flex;
    align-items: center;
    width: $toggle-width;
    height: $toggle-height;
    border-radius: $toggle-height;
    background: $toggle-off-bg;
    border: none;
    cursor: pointer;
    padding: 0;
    flex-shrink: 0;
    transition: background $transition-base;

    &.on {
      background: $toggle-on-bg;
    }

    &:focus-visible {
      outline: 2px solid $color-border-focus;
      outline-offset: 2px;
    }
  }

  .thumb {
    position: absolute;
    left: $toggle-gap;
    width: $toggle-thumb;
    height: $toggle-thumb;
    border-radius: 50%;
    background: $toggle-thumb-bg;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.30);
    transition: transform $transition-base;

    .on & {
      transform: translateX(calc(#{$toggle-width} - #{$toggle-thumb} - #{$toggle-gap} * 2));
    }
  }
</style>
