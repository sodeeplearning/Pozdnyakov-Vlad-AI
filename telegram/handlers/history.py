from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from messages import cleared_message
from .prompt import chatbot


router = Router()


@router.message(Command("clear"))
async def clear_chat_history(message: Message):
    chatbot.clear_history()

    await message.reply(cleared_message)
