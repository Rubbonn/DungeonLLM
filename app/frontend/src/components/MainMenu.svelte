<style lang="scss">
	.main-menu {
		position: relative;
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

	.settings {
		width: 100%;
		height: 100%;
		position: absolute;
		top: 0;
		left: 0;

		&__backdrop {
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			background: rgba(0, 0, 0, .7);
			backdrop-filter: blur(4px);
		}

		&__central-section {
			position: relative;
			max-width: 672px;
			height: 604px;
			margin: 210px auto;
			padding: 32px;
			background: rgba(24, 23, 17, .95);
			border: 1px solid #393628;
			border-radius: 16px;
		}

		&__title {
			font-size: 48px;
			line-height: 60px;
			letter-spacing: -1.58px;
			color: #F1F5F9;
			margin-bottom: 8px;
		}

		&__subtitle {
			font-size: 16px;
			line-height: 24px;
			letter-spacing: 0;
			color: rgba(238, 205, 43, .7);
			font-weight: normal;
			margin-bottom: 16px;
		}

		&__section {
			margin-bottom: 32px;
		}

		&__section-title {
			font-size: 24px;
			font-weight: bold;
			line-height: 30px;
			letter-spacing: -0.6px;
			color: #F1F5F9;
			text-align: left;
			margin-bottom: 24px;

			&::before {
				content: '';
				display: inline-block;
				width: 4px;
				height: 30px;
				background-color: #EECD2B;
				margin-right: 16px;
				vertical-align: middle;
			}
		}

		&__switch-wrapper {
			padding: 24px;
			border: 1px solid #393628;
			border-radius: 12px;
			background-color: rgba(34, 31, 16, .4);
			text-align: left;
			display: flex;
			align-items: center;
			justify-content: space-between;
		}

		&__switch-label {
			font-size: 18px;
			font-weight: bold;
			line-height: 22.5px;
			letter-spacing: 0;
			color: #F1F5F9;
			display: block;
			margin-bottom: 4px;
		}

		&__switch-description {
			font-size: 14px;
			font-weight: normal;
			line-height: 21px;
			color: #94A3B8;
			display: block;
		}

		&__footer {
			display: flex;
			justify-content: center;
			gap: 16px;

			button {
				font-size: 16px;
				line-height: 24px;
				letter-spacing: .8px;
				font-weight: bold;

				img {
					display: inline;
				}
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
			<button class="main-menu__menu-item btn btn-invisible" style:font-size="16px" onclick={() => showSettings = true}><img src="/src/img/icons/cogs.svg" alt="Impostazioni Icon"> IMPOSTAZIONI</button>
		</div>
	</div>
	{#if showSettings}
	<div class="settings" transition:fade={{ duration: 200 }}>
		<div class="settings__backdrop"></div>
		<div class="settings__central-section">
			<h1 class="settings__title">IMPOSTAZIONI</h1>
			<h2 class="settings__subtitle">Personalizza la tua esperienza nel dungeon</h2>
			<div class="settings__section">
				<h3 class="settings__section-title">AUDIO</h3>
				<div class="settings__switch-wrapper">
					<div>
						<label class="settings__switch-label" for="enable-tts">Voci narratore e personaggi</label>
						<small class="settings__switch-description">Abilita il doppiaggio sintetico per un'immersione totale</small>
					</div>
					<input type="checkbox" class="settings__switch" name="enable-tts" id="enable-tts"/>
				</div>
			</div>
			<div class="settings__section">
				<h3 class="settings__section-title">INTERFACCIA</h3>
				<div class="settings__switch-wrapper">
					<div>
						<label class="settings__switch-label" for="enable-subtitles">Sottotitoli</label>
						<small class="settings__switch-description">Mostra il testo durante i dialoghi parlati</small>
					</div>
					<input type="checkbox" class="settings__switch" name="enable-subtitles" id="enable-subtitles"/>
				</div>
			</div>
			<div class="settings__footer">
				<button class="btn btn-secondary" onclick={() => showSettings = false}><img src="/src/img/icons/arrow-back.svg" alt="Indietro Icon"> INDIETRO</button>
				<button class="btn btn-primary"><img src="/src/img/icons/floppy.svg" alt="Salva Icon"> SALVA</button>
			</div>
		</div>
	</div>
	{/if}
</div>

<script lang="ts">
	import { fade } from 'svelte/transition';
	let showSettings = $state(true);
</script>