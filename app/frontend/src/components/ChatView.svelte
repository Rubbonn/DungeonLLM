<style lang="scss">
    .chat-view {
        &__header {
            padding: 12px 32px;
            background-color: rgba(34, 31, 16, .8);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(238, 205, 43, .2);
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
    }
</style>

<div class="chat-view">
    <div class="chat-view__header">
        <div class="chat-view__title">
            <img src="/src/img/icons/logo.svg" class="chat-view__logo" alt="DungeonLLM Logo">
            <h1 class="chat-view__title-text">DungeonLLM</h1>
        </div>
    </div>
</div>

<script lang="ts">
</script>