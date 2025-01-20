from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from src.use_cases.finances.receipts.receipt_use_case import ReceiptUseCase
from src.repositories.receipt_repository import ReceiptRepository
from src.use_cases.finances.receipts.receipt_dto import ReceiptDTO


router = APIRouter()

# Instanciando repositório e caso de uso
receipt_repository = ReceiptRepository()
receipt_use_case = ReceiptUseCase(receipt_repository)

# Rota para criar uma nova receita
@router.post("/receipts")
def create_receipt(receipt_dto: ReceiptDTO):
    return receipt_use_case.create_receipt(receipt_dto)

# Rota para listar todas as receitas
@router.get("/receipts")
def list_receipts():
    return receipt_use_case.list_receipts()

# Rota para buscar uma receita pelo ID
@router.get("/receipts/{receipt_id}")
def get_receipt(receipt_id: str):
    return receipt_use_case.get_receipt(receipt_id)

# Rota para atualizar uma receita
@router.put("/receipts/{receipt_id}")
def update_receipt(receipt_id: str, receipt_dto: ReceiptDTO):
    return receipt_use_case.update_receipt(receipt_id, receipt_dto)

# Rota para deletar uma receita
@router.delete("/receipts/{receipt_id}")
def delete_receipt(receipt_id: str):
    return receipt_use_case.delete_receipt(receipt_id)
