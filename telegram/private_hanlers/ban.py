from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import admins
from bans import ban_user_id, unban_user_id
from messages import incorrect_user_id, user_has_been_banned, user_has_been_unbanned


router = Router()


@router.message(Command("ban"))
async def ban_user(message: Message):
    try:
        _, user_id = message.text.split()
        if message.chat.id in admins:
            ban_user_id(int(user_id))
            await message.reply(user_has_been_banned)

    except TypeError or ValueError:
        await message.reply(incorrect_user_id)


@router.message(Command("unban"))
async def unban_user(message: Message):
    try:
        _, user_id = message.text.split()
        if message.chat.id in admins:
            unban_user_id(int(user_id))
            await message.reply(user_has_been_unbanned)

    except TypeError or ValueError:
        await message.reply(incorrect_user_id)
