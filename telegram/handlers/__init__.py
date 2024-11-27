from aiogram import Router, types
from aiogram.filters.command import Command

from config import hello_message

from . import prompt


router = Router()

router.include_router(prompt.router)


@router.message(Command("start"))
async def start_event(message: types.Message):
    await message.answer(hello_message)
