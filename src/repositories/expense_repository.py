from bson import ObjectId
from src.models.expense_model import ExpenseModel

class ExpenseRepository:
    def save(self, expense):
        expense.save()

    def list_all(self):
        # Converte ObjectId para string em documentos
        expenses = ExpenseModel.objects
        return [self._convert_objectid_to_string(expense.to_mongo().to_dict()) for expense in expenses]

    def find_by_id(self, expense_id: str):
        expense = ExpenseModel.objects(id=expense_id).first()
        if expense:
            return self._convert_objectid_to_string(expense.to_mongo().to_dict())
        return None

    def update(self, expense_id: str, expense_dto):
        updated = ExpenseModel.objects(id=expense_id).update_one(**expense_dto.dict())
        return updated > 0

    def delete(self, expense_id: str):
        deleted = ExpenseModel.objects(id=expense_id).delete()
        return deleted > 0

    @staticmethod
    def _convert_objectid_to_string(document):
        """Converte ObjectId para string em documentos."""
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)
        return document
