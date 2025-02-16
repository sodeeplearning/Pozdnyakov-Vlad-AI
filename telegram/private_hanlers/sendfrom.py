from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import admins
from messages import forwarded_message
from main import bot


router = Router()


@router.message(Command("sf"))
async def send_from_pozd(message: Message):
    splited = message.text.lstrip("/sf").split(":")

    if message.chat.id in admins and len(splited) == 2:
        target_id, text = splited

        target_id = target_id.strip()
        text = text.strip()

        await bot.send_message(
            chat_id=target_id,
            text=text
        )
        await message.reply(forwarded_message)


@router.message(Command("forward"))
async def forward_pozd_answer(message: Message):
    _, target_id = message.split()
    if message.chat.id in admins and message.reply_to_message:
        await message.reply_to_message.forward(chat_id=target_id)
        await message.reply(forwarded_message)
