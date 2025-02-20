from datetime import datetime
from collections import deque

from aiogram.types import Message

from config import max_logs_size


def add_event(user_message: Message, model_answer, print_logs: bool = True):
    logs_deque.append({
        "time": str(datetime.now()),
        "from": user_message.chat.username,
        "user_id": user_message.chat.id,
        "prompt": user_message.text,
        "answer": model_answer
    })
    if print_logs:
        print(logs_deque[-1])
    if len(logs_deque) > max_logs_size:
        logs_deque.popleft()


logs_deque = deque()
history = dict()
quote_history = dict()
