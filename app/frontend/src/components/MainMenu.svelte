<style lang="scss">
    .main-menu {
        height: 100%;
        width: 100%;
        background: no-repeat center/cover url('/src/img/main-menu-background.png');
        color: white;
        overflow:hidden;
        text-align:center;

        &__center {
            padding: 0 24px;
            margin: 171px auto;
            height: 682px;
            display:inline-block;
        }

        &__title-section {
            margin-bottom: 48px;
        }

        &__title {
            display: inline-block;
            font-size:96px;
            font-weight:bold;
            line-height:96px;
            letter-spacing:-4.8px;
            vertical-align:middle;
            background-image: linear-gradient(#FDE68A, #EECD2B 50%, #B45309);
            color: transparent;
            background-clip: text;
            margin-bottom:8px;
        }

        &__subtitle {
            font-size: 14px;
            font-weight: medium;
            line-height: 20px;
            letter-spacing: 5.6px;
            color: #EECD2B;
            opacity: .6;
        }
    }
</style>

<div class="main-menu">
    <div class="main-menu__center">
        <div class="main-menu__title-section">
            <h1 class="main-menu__title">DUNGEONLLM</h1>
            <h2 class="main-menu__subtitle">THE AI MASTER'S DOMAIN</h2>
        </div>
    </div>
</div>