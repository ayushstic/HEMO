from telethon import TelegramClient
import logging
import time
openai_key="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"

api_id="1125689"
api_hash="4772d1792ed194020a8fb06a91ffb8fa"
bot_token="6073171283:AAH8EI4tUFlYrsnXXs59Hbv7aOYYvJSPIek"

bot=TelegramClient("hemo_bot",api_id,api_hash).start(bot_token=bot_token)