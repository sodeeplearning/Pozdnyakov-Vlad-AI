from datetime import datetime
from collections import deque

from aiogram.types import Message

from config import max_logs_size


def add_event(user_message: Message, model_answer):
    logs_deque.append({
        "time": str(datetime.now()),
        "from": user_message.chat.username,
        "prompt": user_message.text,
        "answer": model_answer
    })
    if len(logs_deque) > max_logs_size:
        logs_deque.popleft()


logs_deque = deque()
history = dict()
quote_history = dict()
