from pydantic import BaseModel
from mongoengine import Document, StringField, FloatField

class ReceiptDTO(BaseModel):
    description: str
    amount: float
    category: str
    date: str 