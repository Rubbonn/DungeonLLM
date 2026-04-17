<style lang="scss">
	.chat-view {
		width: 100%;
		height: 100%;
		background-image: radial-gradient(#221F10 80%, #0F0E08);

		&__header {
			padding: 12px 32px;
			background-color: rgba(34, 31, 16, .8);
			backdrop-filter: blur(12px);
			border: 1px solid rgba(238, 205, 43, .2);
			display: flex;
			align-items: center;
			justify-content: space-between;
		}

		&__logo {
			display: inline-block;
			padding: 8px;
			border: 1px solid rgba(238, 205, 43, .4);
			border-radius: 8px;
			background-color: rgba(238, 205, 43, .2);
			box-shadow: 0 0 15px 0 rgba(238, 205, 43, .15);
			margin-right: 16px;
			vertical-align: middle;
		}

		&__title-text {
			display: inline-block;
			font-size: 24px;
			font-weight: bold;
			line-height: 32px;
			letter-spacing: -1.2px;
			color: #EECD2B;
			vertical-align: middle;
		}

		&__top-menu {
			display: flex;
			align-items: center;
		}

		&__mini-info {
			padding: 8px 20px;
			border: 1px solid rgb(238, 205, 43, .2);
			border-radius: 9999px;
			background-color: rgba(34, 31, 16, .8);
			margin-right: 24px;

			span:not(:last-child) {
				margin-right: 16px;
				border-right: 1px solid rgba(238, 205, 43, .2);
			}
		}

		&__gold-text {
			font-size: 14px;
			font-weight: bold;
			line-height: 20px;
			letter-spacing: .35px;
			color: #F1F5F9;
			padding-right: 16px;

			img {
				display: inline-block;
				margin-right: 8px;
			}
		}

		&__player-resume {
			font-size: 14px;
			font-weight: bold;
			line-height: 20px;
			letter-spacing: .35px;
			color: #F1F5F9;

			img {
				display: inline-block;
				margin-right: 8px;
			}
		}

		&__body {
			width: 100%;
			height: 100%;
		}

		&__left-panel {
			width: 100%;
			height: 100%;
		}
	}
</style>

<div class="chat-view">
	<div class="chat-view__header">
		<div class="chat-view__title">
			<img src="/src/img/icons/logo.svg" class="chat-view__logo" alt="DungeonLLM Logo">
			<h1 class="chat-view__title-text">DungeonLLM</h1>
		</div>
		<div class="chat-view__top-menu">
			<div class="chat-view__mini-info">
				<span class="chat-view__gold-text"><img src="/src/img/icons/money.svg" alt="Gold icon">100</span>
				<span class="chat-view__player-resume"><img src="/src/img/icons/level.svg" alt="Level icon">Lvl {player.level}</span>
			</div>
			<div class="chat-view__top-menu-btns">
				<button class="btn btn-secondary"><img src="/src/img/icons/book.svg" alt="Rules icon"> Consulta regole</button>
			</div>
		</div>
	</div>
	<div class="chat-view__body">
		<div class="chat-view__left-panel">
			<PlayerStats />
		</div>
	</div>
	<div class="chat-view__footer"></div>
</div>

<script lang="ts">
	import { createRandomPlayer } from "../utils/testing.svelte.ts";
	import PlayerStats from "./PlayerStats.svelte";
	const player = createRandomPlayer();
</script>