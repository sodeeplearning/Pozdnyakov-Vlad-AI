# Telegram bot interface 

You need GPU to start bot.

## Docker compose

```yml
services:
  bot:
    build:
      context: ../
      dockerfile: ./telegram/Dockerfile

    environment:
        - BOT_TOKEN=0123456789:AAbCDehfG_LqNrBRRVKnbFQMwPCUXX1JZUF  # obtain: @BotFather
        - SUGGESTION_ADMIN=123456789  # admin id for sending post suggestions
        - BEST_CHANNEL=@pozdnyak_ai_best  # channel for post best ai messages

```
