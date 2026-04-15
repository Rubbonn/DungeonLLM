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
			margin-bottom: 16px;
		}

		.btn-primary {
			background-color: #EECD2B;
			color: #221F10;
			box-shadow: 0 0 20px 0 rgba(238, 205, 43, .3);

			&:hover {
				background-color: #F5E070;
				box-shadow: 0 0 28px 4px rgba(245, 224, 112, .45);
			}
		}

		.btn-secondary {
			background-color: rgba(255, 255, 255, .05);
			color: #FFFFFF;
			border: rgba(255, 255, 255, .10) 1px solid;

			&:hover {
				background-color: rgba(255, 255, 255, .12);
				border-color: rgba(255, 255, 255, .25);
				box-shadow: 0 0 20px 0 rgba(255, 255, 255, .08);
			}
		}

		.btn-invisible {
			background-color: transparent;
			color: #94A3B8;
			border: none;

			&:hover {
				color: #F5F0E0;
    			text-shadow: 0 0 12px rgba(245, 240, 224, .3);
			}
		}

		hr {
			border: rgba(255, 255, 255, .10) 1px solid;
			margin-bottom: 16px;
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