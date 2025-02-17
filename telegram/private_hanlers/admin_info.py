from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import admins
from messages import admin_commands_message


router = Router()


@router.message(Command("admin"))
async def get_admin_commands(message: Message):
    if message.chat.id in admins:
        await message.reply(admin_commands_message)
