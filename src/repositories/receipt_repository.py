from bson import ObjectId
from src.models.receipt_model import ReceiptModel  # Importe o modelo de Receipt

class ReceiptRepository:
    def save(self, receipt):
        receipt.save()

    def list_all(self):
        # Converte ObjectId para string em documentos
        receipts = ReceiptModel.objects
        return [self._convert_objectid_to_string(receipt.to_mongo().to_dict()) for receipt in receipts]

    def find_by_id(self, receipt_id: str):
        receipt = ReceiptModel.objects(id=receipt_id).first()
        if receipt:
            return self._convert_objectid_to_string(receipt.to_mongo().to_dict())
        return None

    def update(self, receipt_id: str, receipt_dto):
        updated = ReceiptModel.objects(id=receipt_id).update_one(**receipt_dto.dict())
        return updated > 0

    def delete(self, receipt_id: str):
        deleted = ReceiptModel.objects(id=receipt_id).delete()
        return deleted > 0

    @staticmethod
    def _convert_objectid_to_string(document):
        """Converte ObjectId para string em documentos."""
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)
        return document
    