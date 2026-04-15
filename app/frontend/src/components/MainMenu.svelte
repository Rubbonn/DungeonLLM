<style lang="scss">
	.main-menu {
		height: 100%;
		width: 100%;
		background: no-repeat center/cover url('/src/img/main-menu-background.png');
		color: white;
		overflow: hidden;
		text-align: center;

		&__center-section {
			padding: 0 24px;
			margin: 171px auto;
			height: 682px;
			display:inline-block;
			display: flex;
			flex-direction: column;
			align-items: center;
		}

		&__logo {
			width: 32px;
			height: 40px;
		}

		&__title-section {
			margin-bottom: 48px;
		}

		&__title {
			display: inline-block;
			font-size: 96px;
			font-weight: bold;
			line-height: 96px;
			letter-spacing: -4.8px;
			vertical-align: middle;
			background-image: linear-gradient(#FDE68A, #EECD2B 50%, #B45309);
			color: transparent;
			background-clip: text;
			margin-bottom: 8px;
		}

		&__subtitle {
			font-size: 14px;
			font-weight: medium;
			line-height: 20px;
			letter-spacing: 5.6px;
			color: #EECD2B;
			opacity: .6;
		}

		&__central-section {
			max-width: 464px;
			padding: 32px;
			background: rgba(34, 31, 16, .4);
			backdrop-filter: blur(24px);
			border-radius: 12px;
		}

		&__menu-item {
			font-size: 18px;
			font-weight: bold;
			line-height: 28px;
			letter-spacing: .45px;
			width: 100%;

			img {
				display: inline-block;
			}
		}
	}
</style>

<div class="main-menu">
	<div class="main-menu__center-section">
		<div>
			<img class="main-menu__logo" src="/src/img/icons/shield.svg" alt="DungeonLLM Logo">
		</div>
		<div class="main-menu__title-section">
			<h1 class="main-menu__title">DUNGEONLLM</h1>
			<h2 class="main-menu__subtitle">THE AI MASTER'S DOMAIN</h2>
		</div>
		<div class="main-menu__central-section">
			<button class="main-menu__menu-item btn btn-primary"><img src="/src/img/icons/plus-circle.svg" alt="Nuova Campagna Icon"> NUOVA CAMPAGNA</button>
			<button class="main-menu__menu-item btn btn-secondary"><img src="/src/img/icons/folder.svg" alt="Carica Campagna Icon"> CARICA CAMPAGNA</button>
			<button class="main-menu__menu-item btn btn-secondary"><img src="/src/img/icons/magic-wand.svg" alt="Crea Campagna Icon"> CREA CAMPAGNA</button>
			<hr/>
			<button class="main-menu__menu-item btn btn-invisible" style:font-size="16px"><img src="/src/img/icons/cogs.svg" alt="Impostazioni Icon"> IMPOSTAZIONI</button>
		</div>
	</div>
</div>