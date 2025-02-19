from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import admins
from bot import chatbot
from messages import all_history_cleared


router = Router()


@router.message(Command("absclear"))
async def clear_all_history(message: Message):
    if message.chat.id in admins:
        chatbot.multy_user_history = dict()
        await message.reply(all_history_cleared)
