from mongoengine import Document, StringField, FloatField

class ExpenseModel(Document):
    meta = {'collection': 'expenses'}

    description = StringField(required=True)
    amount = FloatField(required=True)
    category = StringField(required=True)
    date = StringField(required=True)  # Agora é StringField, e não DateTimeField
    user_id = StringField(required=True)