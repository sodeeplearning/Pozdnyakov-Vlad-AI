from datetime import datetime

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from messages import not_reply_message, quoted_message, too_frequently_quote
from config import suggestion_admin, min_latency
from logs_storing import quote_history


router = Router()


@router.message(Command(commands=["quote", "q"]))
async def quote_message(message: Message):
    if message.reply_to_message:
        if message.chat.id not in quote_history or (datetime.now() - quote_history[message.chat.id]).seconds > min_latency:
            await message.reply_to_message.forward(chat_id=suggestion_admin)
            await message.reply(quoted_message)
            quote_history[message.chat.id] = datetime.now()
        else:
            time_remaining = min_latency - (datetime.now() - quote_history[message.chat.id]).seconds
            await message.reply(too_frequently_quote + str(time_remaining))
        return

    await message.reply(not_reply_message)
