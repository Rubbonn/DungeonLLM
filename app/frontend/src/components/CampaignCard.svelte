<script>
  /**
   * id           — unique campaign ID
   * title        — campaign title (e.g. "La Piaga di Ravenloft")
   * thumbnailUrl — path or URL of the small square image
   * charName     — character name
   * charClass    — class string (e.g. "Mago")
   * charLevel    — numeric level
   * lastSave     — human-readable last save string (e.g. "2 ore fa")
   * onPlay       — callback when GIOCA is clicked
   * onDelete     — callback when trash icon is clicked
   */
  let { id, title, thumbnailUrl = '', charName, charClass, charLevel, lastSave, onPlay, onDelete } = $props();

  // Map class names to SVG paths for the small inline icon
  const CLASS_ICONS = {
    Mago:      'M12 2l2.09 6.43H21l-5.47 3.97 2.09 6.43L12 14.9l-5.62 3.93 2.09-6.43L3 8.43h6.91z',
    Guerriero: 'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z',
    Ladro:     'M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z',
    Chierico:  'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4v2z',
    Paladino:  'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z',
    Barbaro:   'M7.5 5.6L10 7 8.6 4.5 10 2 7.5 3.4 5 2l1.4 2.5L5 7zm12 9.8L17 14l1.4 2.5L17 19l2.5-1.4L22 19l-1.4-2.5L22 14zM22 2l-2.5 1.4L17 2l1.4 2.5L17 7l2.5-1.4L22 7l-1.4-2.5zm-7.63 5.29a1.5 1.5 0 00-2.12 0L3 16.54V21h4.46l9.25-9.25a1.5 1.5 0 000-2.12l-2.34-2.34z',
    Bardo:     'M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z',
    Druido:    'M17 8C8 10 5.9 16.17 3.82 28L5.8 28c.91-6.28 3.16-12.13 11.2-14L17 17l4-5-4-4z',
    Monaco:    'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z',
    Ranger:    'M9.5 11L3 17.5V21h3.5L13 14.5 9.5 11zm8.84-7.84l-2.5-2.5c-.78-.78-2.05-.78-2.83 0l-2.38 2.38c-.78.78-.78 2.05 0 2.83l2.5 2.5c.78.78 2.05.78 2.83 0l2.38-2.38c.78-.78.78-2.05 0-2.83z',
    Stregone:  'M12 2l2.09 6.43H21l-5.47 3.97 2.09 6.43L12 14.9l-5.62 3.93 2.09-6.43L3 8.43h6.91z',
    Warlock:   'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z',
  };

  function iconPath(cls) {
    return CLASS_ICONS[cls] ?? CLASS_ICONS['Guerriero'];
  }
</script>

<article class="campaign-card">
  <!-- Thumbnail -->
  <div class="thumb">
    {#if thumbnailUrl}
      <img src={thumbnailUrl} alt="{title} thumbnail" class="thumb-img" />
    {:else}
      <div class="thumb-placeholder" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M9 3H7v2H5V3H3v6h2v11h14V9h2V3h-2v2h-2V3h-2v2h-2V3H9zm7 16H8V9h8v10z" />
        </svg>
      </div>
    {/if}
  </div>

  <!-- Info -->
  <div class="info">
    <h3 class="campaign-title">{title}</h3>

    <p class="campaign-meta">
      <svg class="meta-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d={iconPath(charClass)} />
      </svg>
      <span class="meta-char">{charName}</span>
      <span class="meta-sep">•</span>
      <span>{charClass}</span>
      <span class="meta-sep">•</span>
      <span>Livello {charLevel}</span>
    </p>

    <p class="last-save">Ultimo salvataggio: {lastSave}</p>
  </div>

  <!-- Actions -->
  <div class="actions">
    <button class="delete-btn" onclick={onDelete} aria-label="Elimina campagna {title}">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z" />
      </svg>
    </button>

    <button class="play-btn" onclick={onPlay} aria-label="Gioca a {title}">
      GIOCA
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M8 5v14l11-7z" />
      </svg>
    </button>
  </div>
</article>

<style lang="scss">
  @use '../styles/variables' as *;

  .campaign-card {
    display: flex;
    align-items: center;
    gap: $space-6;
    background: $color-surface;
    border: 1px solid $color-border-subtle;
    border-radius: $radius-lg;
    padding: $space-6;
    transition: border-color $transition-base, background $transition-base;

    &:hover {
      border-color: $color-border;
      background: $color-surface-elevated;
    }
  }

  // ── Thumbnail ────────────────────────────────────────────────────────────────
  .thumb {
    flex-shrink: 0;
    width: $campaign-thumb-size;
    height: $campaign-thumb-size;
    border-radius: $radius-md;
    overflow: hidden;
    background: $color-bg-page;
    border: 1px solid $color-border-subtle;
  }

  .thumb-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  .thumb-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgba($gold-500, 0.20);

    svg {
      width: 32px;
      height: 32px;
    }
  }

  // ── Info ─────────────────────────────────────────────────────────────────────
  .info {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: $space-1;
  }

  .campaign-title {
    font-family: $font-sans;
    font-size: $campaign-title-size;
    font-weight: $font-weight-bold;
    color: $white;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .campaign-meta {
    display: flex;
    align-items: center;
    gap: $space-1;
    font-family: $font-sans;
    font-size: $campaign-meta-size;
    color: $color-accent;
    margin: 0;
    flex-wrap: wrap;
  }

  .meta-icon {
    width: 14px;
    height: 14px;
    flex-shrink: 0;
  }

  .meta-char {
    font-weight: $font-weight-semibold;
  }

  .meta-sep {
    color: $color-text-secondary;
    margin: 0 1px;
  }

  .last-save {
    font-family: $font-sans;
    font-size: $campaign-save-size;
    font-style: italic;
    color: $color-text-secondary;
    margin: 0;
  }

  // ── Actions ──────────────────────────────────────────────────────────────────
  .actions {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: $space-3;
  }

  .delete-btn {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: none;
    border: none;
    cursor: pointer;
    color: $color-text-secondary;
    border-radius: $radius-sm;
    transition: color $transition-base, background $transition-base;

    svg {
      width: 18px;
      height: 18px;
    }

    &:hover {
      color: $color-btn-danger-bg;
      background: $color-danger-icon-bg;
    }
  }

  .play-btn {
    display: flex;
    align-items: center;
    gap: $space-1;
    padding: $space-2 $space-5;
    background: $color-btn-primary-bg;
    border: none;
    border-radius: $radius-md;
    cursor: pointer;
    font-family: $font-serif;
    font-size: $font-size-btn;
    font-weight: $font-weight-black;
    letter-spacing: $letter-spacing-btn;
    color: $color-btn-primary-text;
    white-space: nowrap;
    transition: $transition-btn;

    svg {
      width: 16px;
      height: 16px;
    }

    &:hover {
      background: $color-btn-primary-hover-bg;
      box-shadow: $glow-btn-primary;
      transform: translateY(-1px);
    }

    &:active {
      transform: translateY(1px);
    }
  }
</style>
