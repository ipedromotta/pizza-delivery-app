from typing import List
from pydantic import BaseModel
from schemas import ItemSchema


class ResponseOrderSchema(BaseModel):
    id: int
    status: str
    preco: float
    itens: List[ItemSchema]
    