<style lang="scss">
    .chat {
        &__messages {
            padding: 32px;
            overflow: hidden;
            overflow-y: scroll;
        }

        &__message {
            margin-bottom: 32px;
            display: flex;
            align-items: flex-start;

            &--user {
                flex-direction: row-reverse;

                .chat__message-avatar {
                    margin-left: 16px;
                }

                .chat__message-content {
                    background-color: #EECD2B;
                    border-radius: 12px 0 12px 12px;
                }
            }

            &--assistant {
                flex-direction: row;

                .chat__message-avatar {
                    margin-right: 16px;
                }

                .chat__message-content {
                    background-image: radial-gradient(rgba(238, 205, 43, .05), rgba(238, 205, 43, 0));
                    background-color: #F4ECD8;
                    border: 1px solid #D4C4A1;
                    border-radius: 0 12px 12px 12px;
                }
            }
        }

        &__message-avatar {
            width: 48px;
            height: 48px;
            border-radius: 9999px;
            background-color: #221F10;
            border: 2px solid #EECD2B;
            box-shadow: 0 0 0 4px rgba(238, 205, 43, .10);
        }

        &__message-content {
            padding: 20px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, .25);
            color: #1E293B;
            font-size: 18px;
            line-height: 29.3px;
            letter-spacing: 0;

            &::before {
                content: "";
                border-top: 10px solid #D4C4A1;
                border-left: 10px solid #D4C4A1;
                display: block;
            }
        }
    }
</style>

<div class="chat">
    <div class="chat__messages">
        {#each messages as { role, content }}
            <div class="chat__message chat__message--{role}">
                <img class="chat__message-avatar" src="https://gravatar.com/avatar/ed7dc7747f1fe0e658369a66450151b8?s=400&d=retro&r=x" alt="{role} avatar">
                <div class="chat__message-content">{content}</div>
            </div>
        {/each}
    </div>
    <div class="chat__input">
    </div>
</div>

<script lang="ts">
    import { createRandomMessages } from "../utils/testing.svelte.ts";
    const messages = $state(createRandomMessages(10));
</script>