from pydantic import BaseModel

class ExpenseDTO(BaseModel):
    description: str
    amount: float
    category: str
    date: str
    user_id: str  # Campo obrigatório
