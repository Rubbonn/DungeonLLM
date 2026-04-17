<style lang="scss">
	.player-stats {
		padding: 24px;
		background-color: rgba(34, 31, 16, .6);
		backdrop-filter: blur(12px);
		border: 1px solid rgba(238, 205, 43, .1);
		max-width: 25%;
		height: 100%;

		&__profile {
			display: flex;
			flex-direction: column;
			align-items: center;
			border-bottom: 1px solid rgba(238, 205, 43, .1);
			margin-bottom: 24px;
		}

		&__player-picture {
			width: 96px;
			height: 96px;
			padding: 4px;
			background-color: #221F10;
			border: 2px solid #EECD2B;
			border-radius: 9999px;
			box-shadow: 0 0 0 4px rgba(238, 205, 43, .1);
			margin-bottom: 16px;
		}

		&__player-name {
			font-size: 18px;
			font-weight: bold;
			line-height: 28px;
			letter-spacing: -.45px;
			color: #FFFFFF;
		}

		&__player-level {
			font-size: 12px;
			font-weight: medium;
			line-height: 16px;
			letter-spacing: 1.2px;
			color: #EECD2B;
			margin-bottom: 25px;
		}

		&__section {
			margin-bottom: 24px;
		}

		&__section-title {
			font-size: 10px;
			font-weight: bold;
			line-height: 15px;
			letter-spacing: 2px;
			color: rgba(238, 205, 43, .6);
			margin-bottom: 16px;

			&::before {
				content: '';
				display: inline-block;
				width: 32px;
				height: 1px;
				background-color: rgba(238, 205, 43, .2);
				margin-right: 8px;
				vertical-align: middle;
			}
		}

		&__stat-name {
			font-size: 12px;
			font-weight: bold;
			line-height: 16px;
			letter-spacing: 0;
			color: #F1F5F9;

			img {
				display: inline-block;
				margin-right: 4px;
			}
		}

		&__stat-value {
			font-size: 12px;
			font-weight: bold;
			line-height: 16px;
			letter-spacing: 0;
			color: #F1F5F9;
			float: right;
		}

		&__stat-bar {
			display: block;
			width: 100%;
			height: 8px;
			background-color: rgba(30, 41, 59, .5);
			border: 1px solid rgba(255, 255, 255, .05);
			border-radius: 9999px;
			margin-top: 6px;

			&::before {
				content: '';
				display: block;
				width: var(--hp-percentage, 100%);
				height: 100%;
				background-image: linear-gradient(90deg, #DC2626, #F87171);
				box-shadow: 0 0 8px 0 rgba(220, 38, 38, .5);
			}
		}
	}
</style>

<div class="player-stats">
	<div class="player-stats__profile">
		<img src="https://gravatar.com/avatar/ed7dc7747f1fe0e658369a66450151b8?s=400&d=retro&r=x" alt="Player" class="player-stats__player-picture">
		<span class="player-stats__player-name">{player.name}</span>
		<span class="player-stats__player-level">LEVEL {player.level}</span>
	</div>
	<div class="player-stats__section">
		<span class="player-stats__section-title">VITALITY</span>
		<div class="player-stats__section-content">
			<div class="player-stats__stat">
				<span class="player-stats__stat-name"><img src="/src/img/icons/heart.svg" alt="Heart Icon"> HP</span>
				<span class="player-stats__stat-value">{player.hit_points} / {player.hit_points}</span>
				<hr class="player-stats__stat-bar" style:--hp-percentage={`${player.hit_points / player.hit_points * 100}%`}/>
			</div>
		</div>
	</div>
</div>

<script lang="ts">
	import { createRandomPlayer } from "../utils/testing.svelte.ts";
	const player = createRandomPlayer();
</script>