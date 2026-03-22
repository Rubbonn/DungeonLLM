<script>
  let { placeholder = '', value = $bindable('') } = $props();
</script>

<input
  class="form-input"
  type="text"
  {placeholder}
  bind:value
/>

<style lang="scss">
  @use '../styles/variables' as *;

  .form-input {
    display: block;
    width: 100%;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-md;
    padding: $space-5 $space-6;
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-primary;
    outline: none;
    transition: border-color $transition-base;

    &::placeholder {
      color: $color-placeholder;
    }

    &:focus {
      border-color: $color-border-focus;
    }
  }
</style>
