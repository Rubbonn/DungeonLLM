<style lang="scss">
    :global {
        @font-face {
            font-family: 'Work Sans';
            font-style: normal;
            src: url('/src/font/WorkSans-VariableFont_wght.ttf') format('truetype');
        }

        html, body {
            margin:0;
            padding:0;
            overflow:hidden;

            font-family: 'Work Sans';
        }
    }
    :global(#app) {
        width:1280px;
        height:1024px;
    }
</style>

{#if contextState.currentPage === 'main-menu'}
<MainMenu/>
{/if}

<script lang="ts">
import { contextState } from './states/context.svelte.ts';
import MainMenu from './components/MainMenu.svelte';
</script>