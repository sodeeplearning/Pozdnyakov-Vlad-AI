from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import best_channel, admins


router = Router()


@router.message(Command(commands=["post", "p"]))
async def post_message(message: Message):
    if message.reply_to_message and message.chat.id in admins:
        await message.reply_to_message.forward(chat_id=best_channel)
