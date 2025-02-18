import json
import os

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from logs_storing import logs_deque
from config import admins
from messages import cleared_logs_message


router = Router()


@router.message(Command("checklogs"))
async def check_logs(message: Message):
    if message.chat.id in admins:
        await message.reply(str(logs_deque))


@router.message(Command("savelogs"))
async def save_logs(message: Message):
    if message.chat.id in admins:
        with open("logs.json", "w", encoding="utf-8") as json_file:
            json.dump(list(logs_deque), json_file, ensure_ascii=False, indent=4)

        await message.answer_document(FSInputFile("logs.json"))
        os.remove("logs.json")


@router.message(Command("clearlogs"))
async def clear_logs(message: Message):
    if message.chat.id in admins:
        logs_deque.clear()
        await message.reply(cleared_logs_message)
