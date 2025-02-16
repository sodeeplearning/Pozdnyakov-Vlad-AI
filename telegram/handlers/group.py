from datetime import datetime

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from messages import before_answer_message, too_frequently_message
from config import min_latency
from logs_storing import add_event, history

from .prompt import chatbot


router = Router()


@router.message(Command("ask"))
async def answer_to_message_in_group(message: Message):
    if message.chat.id not in history or (datetime.now() - history[message.chat.id]).seconds > min_latency:
        base_answer = await message.answer(before_answer_message)

        model_answer = chatbot(prompt=message.text)

        await base_answer.delete()
        await message.reply(model_answer)

        history[message.chat.id] = datetime.now()
        add_event(message, model_answer)
    else:
        time_remaining = min_latency - (datetime.now() - history[message.chat.id]).seconds
        await message.reply(too_frequently_message + str(time_remaining))