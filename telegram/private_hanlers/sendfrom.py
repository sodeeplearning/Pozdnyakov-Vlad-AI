from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import admins
from main import bot


router = Router()


@router.message(Command("sf"))
async def send_from_pozd(message: Message):
    splited = message.text.lstrip("/sf").split(":")

    if int(message.chat.id) in admins and len(splited) == 2:
        target_id, text = splited

        target_id = target_id.strip()
        text = text.strip()

        await bot.send_message(
            chat_id=target_id,
            text=text
        )
