<script>
  import MainTopBar from '../components/MainTopBar.svelte';
  import CampaignCard from '../components/CampaignCard.svelte';
  import ConfirmDialog from '../components/ConfirmDialog.svelte';

  let { onBack } = $props();

  // ── Demo campaign data ───────────────────────────────────────────────────────
  let campaigns = $state([
    {
      id: 1,
      title: 'La Piaga di Ravenloft',
      thumbnailUrl: '',
      charName: 'Eldrin',
      charClass: 'Mago',
      charLevel: 12,
      lastSave: '2 ore fa',
    },
    {
      id: 2,
      title: 'Miniere di Phandelver',
      thumbnailUrl: '',
      charName: 'Thrain',
      charClass: 'Guerriero',
      charLevel: 5,
      lastSave: 'Ieri',
    },
    {
      id: 3,
      title: 'Il Trono di Spade',
      thumbnailUrl: '',
      charName: 'Arya',
      charClass: 'Ladro',
      charLevel: 8,
      lastSave: '3 giorni fa',
    },
    {
      id: 4,
      title: 'Cripte di Oghma',
      thumbnailUrl: '',
      charName: 'Silas',
      charClass: 'Chierico',
      charLevel: 3,
      lastSave: '12 giorni fa',
    },
  ]);

  // ── Delete confirmation dialog ───────────────────────────────────────────────
  let deleteDialog = $state({ open: false, targetId: null });

  function askDelete(id) {
    deleteDialog = { open: true, targetId: id };
  }

  function cancelDelete() {
    deleteDialog = { open: false, targetId: null };
  }

  function confirmDelete() {
    campaigns = campaigns.filter((c) => c.id !== deleteDialog.targetId);
    deleteDialog = { open: false, targetId: null };
  }

  function handlePlay(id) {
    // TODO: navigate to game page for campaign `id`
    console.log('Play campaign', id);
  }
</script>

<div class="load-campaign" class:blurred={deleteDialog.open}>
  <MainTopBar />

  <div class="page-content">
    <!-- Back link -->
    <button class="back-link" onclick={onBack}>
      <svg class="back-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
      </svg>
      Indietro al Menù Principale
    </button>

    <!-- Page header -->
    <div class="page-header">
      <h1 class="page-title">Carica Campagna</h1>
      <p class="page-subtitle">Le tue cronache ti attendono. Riprendi il viaggio da dove l'hai interrotto.</p>
    </div>

    <!-- Campaign list -->
    <div class="campaign-list" role="list">
      {#each campaigns as campaign (campaign.id)}
        <div role="listitem">
          <CampaignCard
            {...campaign}
            onPlay={() => handlePlay(campaign.id)}
            onDelete={() => askDelete(campaign.id)}
          />
        </div>
      {/each}

      {#if campaigns.length === 0}
        <p class="empty-state">Nessuna campagna salvata. Inizia una nuova avventura!</p>
      {/if}
    </div>

    <!-- New Adventure card -->
    <button class="new-adventure-card" onclick={onBack}>
      <div class="na-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M19 13H13v6h-2v-6H5v-2h6V5h2v6h6v2z" />
        </svg>
      </div>
      <div class="na-text">
        <span class="na-title">Nuova Avventura</span>
        <span class="na-subtitle">Inizia una nuova cronaca generata dall'IA</span>
      </div>
    </button>
  </div>

  <!-- Footer -->
  <footer class="page-footer">
    <p class="footer-copy">© 2024 DungeonLLM – Master IA per le tue avventure dark fantasy</p>
  </footer>
</div>

<!-- Confirmation dialog (rendered outside .blurred so it stays sharp) -->
<ConfirmDialog
  open={deleteDialog.open}
  title="Elimina Campagna"
  body="Sei sicuro di voler eliminare questa campagna?"
  bodyNote="Questa azione è irreversibile e tutti i progressi andranno perduti."
  confirmText="Elimina"
  cancelText="Annulla"
  variant="danger"
  onConfirm={confirmDelete}
  onCancel={cancelDelete}
/>

<style lang="scss">
  @use '../styles/variables' as *;

  // ── Page shell ───────────────────────────────────────────────────────────────
  .load-campaign {
    min-height: 100vh;
    background-color: $color-bg-page;
    color: $color-text-primary;
    display: flex;
    flex-direction: column;
    transition: filter $transition-base;

    &.blurred {
      filter: blur(2px) brightness(0.55);
      pointer-events: none;
    }
  }

  // ── Scrollable content ───────────────────────────────────────────────────────
  .page-content {
    flex: 1;
    max-width: $campaign-max-width;
    width: 100%;
    margin: 0 auto;
    padding: $space-10 $space-9 $space-13;
  }

  // ── Back link ─────────────────────────────────────────────────────────────────
  .back-link {
    display: inline-flex;
    align-items: center;
    gap: $space-2;
    background: none;
    border: none;
    cursor: pointer;
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-accent;
    padding: 0;
    margin-bottom: $space-9;
    transition: opacity $transition-base;

    &:hover {
      opacity: 0.75;
    }
  }

  .back-icon {
    width: 18px;
    height: 18px;
  }

  // ── Page header ───────────────────────────────────────────────────────────────
  .page-header {
    margin-bottom: $space-9;
  }

  .page-title {
    font-family: $font-sans;
    font-size: clamp(28px, 4vw, 40px);
    font-weight: $font-weight-black;
    color: $white;
    margin: 0 0 $space-3;
    line-height: 1.1;
  }

  .page-subtitle {
    font-family: $font-sans;
    font-size: $font-size-body;
    color: $color-text-primary;
    margin: 0;
    line-height: 1.5;
  }

  // ── Campaign list ─────────────────────────────────────────────────────────────
  .campaign-list {
    display: flex;
    flex-direction: column;
    gap: $space-4;
    margin-bottom: $space-9;
  }

  .empty-state {
    font-family: $font-sans;
    font-size: $font-size-body;
    font-style: italic;
    color: $color-text-secondary;
    text-align: center;
    padding: $space-9 0;
  }

  // ── Nuova Avventura card ──────────────────────────────────────────────────────
  .new-adventure-card {
    display: flex;
    align-items: center;
    gap: $space-6;
    width: 100%;
    padding: $space-6;
    background: none;
    border: 1.5px dashed $color-border;
    border-radius: $radius-lg;
    cursor: pointer;
    text-align: left;
    transition: border-color $transition-base, background $transition-base;

    &:hover {
      border-color: $color-accent;
      background: rgba($gold-500, 0.04);
    }
  }

  .na-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: rgba($gold-500, 0.12);
    color: $color-accent;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;

    svg {
      width: 22px;
      height: 22px;
    }
  }

  .na-text {
    display: flex;
    flex-direction: column;
    gap: $space-1;
  }

  .na-title {
    font-family: $font-sans;
    font-size: $campaign-title-size;
    font-weight: $font-weight-bold;
    color: $white;
  }

  .na-subtitle {
    font-family: $font-sans;
    font-size: $font-size-caption;
    color: $color-text-secondary;
  }

  // ── Footer ───────────────────────────────────────────────────────────────────
  .page-footer {
    padding: $space-7 $space-9;
    border-top: 1px solid $color-border-subtle;
    text-align: center;
  }

  .footer-copy {
    font-family: $font-sans;
    font-size: $font-size-caption;
    color: $color-text-secondary;
    margin: 0;
  }
</style>
