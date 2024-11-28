from aiogram import Router, types, F

from pozdnyakov.chatbot import PozdnyakovChatBot


router = Router()

chatbot = PozdnyakovChatBot(
    save_history=False,
    print_dialogues=True
)


@router.message(F.text)
async def send_answer(message: types.Message):
    model_answer = chatbot(prompt=message.text)
    await message.answer(model_answer)
