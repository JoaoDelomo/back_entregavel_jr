from mongoengine import Document, StringField, FloatField, DateField

class ReceiptModel(Document):
    meta = {'collection': 'receipts'}

    description = StringField(required=True)
    amount = FloatField(required=True)
    category = StringField(required=True)
    date = StringField(required=True)  # Agora a data é uma string
