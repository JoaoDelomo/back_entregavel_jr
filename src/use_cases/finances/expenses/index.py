from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from src.use_cases.finances.expenses.expense_use_case import ExpensesUseCase
from src.repositories.expense_repository import ExpenseRepository

router = APIRouter()

# DTO para validação de dados de Expenses
class ExpenseDTO(BaseModel):
    description: str
    amount: float
    category: str
    date: date
    user_id: str

# Instanciando repositório e caso de uso
expenses_repository = ExpenseRepository()
expenses_use_case = ExpensesUseCase(expenses_repository)

# Rota para criar uma nova despesa
@router.post("/expenses")
def create_expense(expense_dto: ExpenseDTO):
    return expenses_use_case.create_expense(expense_dto)

# Rota para listar todas as despesas
@router.get("/expenses")
def list_expenses():
    return expenses_use_case.get_all_expenses()

# Rota para buscar uma despesa pelo ID
@router.get("/expenses/{expense_id}")
def get_expense(expense_id: str):
    return expenses_use_case.get_expense(expense_id)

# Rota para atualizar uma despesa
@router.put("/expenses/{expense_id}")
def update_expense(expense_id: str, expense_dto: ExpenseDTO):
    return expenses_use_case.update_expense(expense_id, expense_dto)

# Rota para deletar uma despesa
@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: str):
    return expenses_use_case.delete_expense(expense_id)
