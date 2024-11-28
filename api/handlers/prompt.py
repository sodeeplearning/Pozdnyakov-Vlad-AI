from fastapi import APIRouter

from api.models import TextModel

from pozdnyakov.chatbot import PozdnyakovChatBot


router = APIRouter()

chatbot = PozdnyakovChatBot()


@router.post("/prompt/text")
async def prompt_text(body: TextModel) -> TextModel:
    model_answer = chatbot(body.text)
    return TextModel(text=model_answer)
