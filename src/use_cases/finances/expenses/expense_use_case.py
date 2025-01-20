from repositories.expense_repository import ExpenseRepository
from src.models.expense_model import ExpenseModel
from src.use_cases.finances.expenses.expense_dto import ExpenseDTO
from datetime import datetime, date


class ExpensesUseCase:
    def __init__(self, expense_repository: ExpenseRepository):
        self.expense_repository = expense_repository

    def create_expense(self, expense_dto: ExpenseDTO):
        # Verifica se a data já é uma string, e caso contrário, formata a data como string
        if isinstance(expense_dto.date, (datetime, date)):
            expense_dto.date = expense_dto.date.strftime("%Y-%m-%d")
        
        expense = ExpenseModel(
            description=expense_dto.description,
            amount=expense_dto.amount,
            category=expense_dto.category,
            date=expense_dto.date,  # Agora a data é uma string no formato correto
            user_id=expense_dto.user_id,
        )
        self.expense_repository.save(expense)
        return {"status": "success", "message": "Expense created successfully"}

    def get_all_expenses(self):
        expenses = self.expense_repository.list_all()
        return {"status": "success", "data": expenses}

    def get_expense(self, expense_id: str):
        expense = self.expense_repository.find_by_id(expense_id)
        if expense:
            return {"status": "success", "data": expense}
        return {"status": "error", "message": "Expense not found"}

    def update_expense(self, expense_id: str, expense_dto: ExpenseDTO):
        # Verifica se a 'date' já é uma string ou um objeto datetime e a converte para string no formato desejado
        if isinstance(expense_dto.date, datetime):
            expense_dto.date = expense_dto.date.strftime("%Y-%m-%d")
        elif isinstance(expense_dto.date, date):  # Caso seja uma data
            expense_dto.date = expense_dto.date.strftime("%Y-%m-%d")
        
        # Agora, você pode chamar o repositório para atualizar a despesa
        updated = self.expense_repository.update(expense_id, expense_dto)
        if updated:
            return {"status": "success", "message": "Despesa atualizada com sucesso"}
        return {"status": "error", "message": "Despesa não encontrada"}
    
    def delete_expense(self, expense_id: str):
        deleted = self.expense_repository.delete(expense_id)
        if deleted:
            return {"status": "success", "message": "Expense deleted successfully"}
        return {"status": "error", "message": "Expense not found"}
