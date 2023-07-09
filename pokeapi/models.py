from pydantic import BaseModel
from typing import List

class Pokemon(BaseModel):
    id: int
    name: str
    types: List[str]