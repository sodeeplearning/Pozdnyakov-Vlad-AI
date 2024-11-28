from pydantic import BaseModel


class TextModel(BaseModel):
    text: str
