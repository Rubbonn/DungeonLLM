<script lang="ts">
  import ToggleSwitch from './ToggleSwitch.svelte';
  import type { SettingsValues } from '../lib/types.js';

  /**
   * open     — controls visibility
   * onClose  — callback fired when INDIETRO is clicked or backdrop clicked
   * onSave   — callback fired when SALVA is clicked (receives current settings)
   */
  interface Props {
    open?: boolean;
    onClose?: () => void;
    onSave?: (settings: SettingsValues) => void;
  }

  let { open = false, onClose, onSave }: Props = $props();

  // ── Settings state ────────────────────────────────────────────────────────────
  let voiceEnabled     = $state<boolean>(true);
  let subtitlesEnabled = $state<boolean>(false);

  function handleSave(): void {
    onSave?.({ voiceEnabled, subtitlesEnabled });
    onClose?.();
  }

  function handleBackdrop(e: MouseEvent): void {
    if (e.target === e.currentTarget) onClose?.();
  }

  function handleKeydown(e: KeyboardEvent): void {
    if (e.key === 'Escape') onClose?.();
  }
</script>

{#if open}
  <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
  <div
    class="backdrop"
    role="dialog"
    aria-modal="true"
    aria-labelledby="settings-title"
    tabindex="-1"
    onmousedown={handleBackdrop}
    onkeydown={handleKeydown}
  >
    <div class="modal">
      <!-- Heading -->
      <h2 class="modal-title" id="settings-title">IMPOSTAZIONI</h2>
      <p class="modal-subtitle">Personalizza la tua esperienza nel dungeon</p>

      <!-- AUDIO section -->
      <section class="settings-section">
        <h3 class="section-heading">AUDIO</h3>

        <div class="setting-row">
          <div class="setting-info">
            <span class="setting-label">Voci narratore e personaggi</span>
            <span class="setting-desc">Abilita il doppiaggio sintetico per un&apos;immersione totale</span>
          </div>
          <ToggleSwitch bind:checked={voiceEnabled} label="Voci narratore e personaggi" />
        </div>
      </section>

      <!-- INTERFACCIA section -->
      <section class="settings-section">
        <h3 class="section-heading">INTERFACCIA</h3>

        <div class="setting-row">
          <div class="setting-info">
            <span class="setting-label">Sottotitoli</span>
            <span class="setting-desc">Mostra il testo durante i dialoghi parlati</span>
          </div>
          <ToggleSwitch bind:checked={subtitlesEnabled} label="Sottotitoli" />
        </div>
      </section>

      <!-- Actions -->
      <div class="modal-actions">
        <button class="btn-back" onclick={onClose}>
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
          </svg>
          INDIETRO
        </button>

        <button class="btn-save" onclick={handleSave}>
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M17 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V7l-4-4zm-5 16c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm3-10H5V5h10v4z" />
          </svg>
          SALVA
        </button>
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
    background: rgba(0, 0, 0, 0.78);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: $z-modal;
    padding: $space-9;
  }

  // ── Modal card ───────────────────────────────────────────────────────────────
  .modal {
    background: $color-surface;
    border: 1px solid $color-border;
    border-radius: 20px;
    padding: $space-12 $space-11 $space-10;
    width: 100%;
    max-width: 640px;
    display: flex;
    flex-direction: column;
    gap: $space-7;
  }

  // ── Heading ──────────────────────────────────────────────────────────────────
  .modal-title {
    font-family: $font-sans;
    font-size: clamp(28px, 4vw, 36px);
    font-weight: $font-weight-black;
    color: $white;
    text-align: center;
    letter-spacing: 3px;
    margin: 0;
    line-height: 1;
  }

  .modal-subtitle {
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-accent;
    text-align: center;
    margin: -$space-4 0 0;
    line-height: 1.4;
  }

  // ── Section ──────────────────────────────────────────────────────────────────
  .settings-section {
    display: flex;
    flex-direction: column;
    gap: $space-4;
  }

  .section-heading {
    font-family: $font-sans;
    font-size: 15px;
    font-weight: $font-weight-black;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: $white;
    margin: 0;
    padding-left: $space-4;
    border-left: 3px solid $color-accent;
    line-height: 1.2;
  }

  // ── Setting row ──────────────────────────────────────────────────────────────
  .setting-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: $space-9;
    background: $color-surface-elevated;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-lg;
    padding: $space-7 $space-8;
  }

  .setting-info {
    display: flex;
    flex-direction: column;
    gap: $space-1;
    min-width: 0;
  }

  .setting-label {
    font-family: $font-sans;
    font-size: $font-size-body;
    font-weight: $font-weight-bold;
    color: $white;
    line-height: 1.3;
  }

  .setting-desc {
    font-family: $font-sans;
    font-size: $font-size-caption;
    color: $color-text-secondary;
    line-height: 1.45;
  }

  // ── Actions ──────────────────────────────────────────────────────────────────
  .modal-actions {
    display: flex;
    justify-content: center;
    gap: $space-4;
    margin-top: $space-3;
  }

  %pill-btn {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    padding: $space-4 $space-9;
    border-radius: 999px;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-btn;
    font-weight: $font-weight-black;
    letter-spacing: $letter-spacing-btn;
    transition: background $transition-base, box-shadow $transition-base, transform $transition-fast;

    svg {
      width: 16px;
      height: 16px;
      flex-shrink: 0;
    }

    &:active {
      transform: translateY(1px);
    }
  }

  .btn-back {
    @extend %pill-btn;
    background: $color-surface-elevated;
    color: $white;
    border: 1px solid $color-border;

    &:hover {
      background: $color-border;
    }
  }

  .btn-save {
    @extend %pill-btn;
    background: $color-btn-primary-bg;
    color: $color-btn-primary-text;

    &:hover {
      background: $color-btn-primary-hover-bg;
      box-shadow: $glow-btn-primary;
      transform: translateY(-1px);
    }
  }
</style>
