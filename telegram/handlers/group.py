from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from utils.sendans import send_model_answer


router = Router()


@router.message(Command("ask"))
async def answer_to_message_in_group(message: Message):
    await send_model_answer(message)
