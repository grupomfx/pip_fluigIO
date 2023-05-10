from typing import List

from pydantic import BaseModel, Field


class Item(BaseModel):
    field: str
    value: str


class CardData(BaseModel):
    item: List[Item] = Field(default_factory=list)
