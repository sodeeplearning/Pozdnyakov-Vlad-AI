from aiogram import Router, types, F

from utils.sendans import send_model_answer


router = Router()


@router.message(F.text, F.chat.type == "private")
async def send_answer(message: types.Message):
    await send_model_answer(message)
