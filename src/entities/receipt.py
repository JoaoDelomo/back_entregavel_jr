from pydantic import BaseModel
from typing import Optional

class Receipt(BaseModel):
    _id: str
    user_id: str
    amount: float
    description: Optional[str]
    category: Optional[str]
    date: str
