from aiogram import Router, types, F

from pozdnyakov.chatbot import PozdnyakovChatBot
from config import before_answer_message


router = Router()

chatbot = PozdnyakovChatBot(
    save_history=False,
    print_dialogues=True
)


@router.message(F.text)
async def send_answer(message: types.Message):
    base_answer = await message.answer(before_answer_message)

    model_answer = chatbot(prompt=message.text)
    await base_answer.delete()

    await message.reply(model_answer)
