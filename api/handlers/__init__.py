from fastapi import APIRouter

from . import prompt

router = APIRouter()

router.include_router(prompt.router)


@router.get("/")
async def start_event():
    return "Меня зовут Влад Поздняков, и я радостью отвечу на все ваши вопросы!"
