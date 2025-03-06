from pydantic import BaseModel
from typing import List


class ItemSchema(BaseModel):
    id: int
    title: str
    price: float


class ItemRequestSchema(BaseModel):
    items: List[int]