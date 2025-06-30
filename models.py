from typing import Any
from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    id: int
    title: str
    img: str
    content: str
    author: str
    created_at: str

class SDeleteFilter(BaseModel):
    id: int