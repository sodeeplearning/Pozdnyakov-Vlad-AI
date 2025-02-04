from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from messages import not_reply_message, quoted_message
from config import suggestion_admin, best_channel


router = Router()


@router.message(Command(commands=["quote", "q"]))
async def quote_message(message: Message):
    if message.reply_to_message:
        await message.reply_to_message.forward(chat_id=suggestion_admin)
        await message.reply(quoted_message)
        return

    await message.reply(not_reply_message)


@router.message(Command(commands=["post", "p"]))
async def post_message(message: Message):
    if message.reply_to_message and message.chat.id == int(suggestion_admin):
        await message.reply_to_message.forward(chat_id=best_channel)
