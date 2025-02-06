from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from .prompt import chatbot
from messages import before_answer_message


router = Router()


@router.message(Command("ask"))
async def answer_to_message_in_group(message: Message):
    base_answer = await message.answer(before_answer_message)

    model_answer = chatbot(prompt=message.text)

    await base_answer.delete()
    await message.reply(model_answer)
