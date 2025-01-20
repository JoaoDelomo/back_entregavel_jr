from pydantic import BaseModel
from typing import Optional

class Expense(BaseModel):
    _id: str
    user_id: str
    amount: float
    description: Optional[str]
    category: Optional[str]
    date: str
