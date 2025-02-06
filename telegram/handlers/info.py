from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from messages import info_message


router = Router()


@router.message(Command("info"))
async def get_info(message: Message):
    await message.reply(info_message)
