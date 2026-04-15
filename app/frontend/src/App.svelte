<style lang="scss">
    :global {
        @font-face {
            font-family: 'Work Sans';
            font-style: normal;
            src: url('/src/font/WorkSans-VariableFont_wght.ttf') format('truetype');
        }

        html, body {
            font-family: 'Work Sans';
        }

        .btn {
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            padding: 14px 14px;
            border: none;
        }

        .btn-primary {
            background-color: #EECD2B;
            color: #221F10;
            box-shadow: 0 0 20px 0 rgba(238, 205, 43, .3);

            &:hover {
            }
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
import contextState from './states/context.svelte.ts';
import MainMenu from './components/MainMenu.svelte';
</script>