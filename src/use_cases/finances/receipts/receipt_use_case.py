from src.repositories.receipt_repository import ReceiptRepository
from src.models.receipt_model import ReceiptModel
from src.use_cases.finances.receipts.receipt_dto import ReceiptDTO

class ReceiptUseCase:
    def __init__(self, receipt_repository: ReceiptRepository):
        self.receipt_repository = receipt_repository

    def create_receipt(self, receipt_dto: ReceiptDTO):
        receipt = ReceiptModel(
            description=receipt_dto.description,
            amount=receipt_dto.amount,
            category=receipt_dto.category,
            date=receipt_dto.date
        )
        self.receipt_repository.save(receipt)
        return {"status": "success", "message": "Receita criada com sucesso"}
    
    def list_receipts(self):
        receipts = self.receipt_repository.list_all()
        return {"status": "success", "data": receipts}

    def get_receipt(self, receipt_id: str):
        receipt = self.receipt_repository.find_by_id(receipt_id)
        if receipt:
            return {"status": "success", "data": receipt}
        return {"status": "error", "message": "Receita não encontrada"}

    def update_receipt(self, receipt_id: str, receipt_dto: ReceiptDTO):
        updated = self.receipt_repository.update(receipt_id, receipt_dto)
        if updated:
            return {"status": "success", "message": "Receita atualizada com sucesso"}
        return {"status": "error", "message": "Receita não encontrada"}

    def delete_receipt(self, receipt_id: str):
        deleted = self.receipt_repository.delete(receipt_id)
        if deleted:
            return {"status": "success", "message": "Receita excluída com sucesso"}
        return {"status": "error", "message": "Receita não encontrada"}
