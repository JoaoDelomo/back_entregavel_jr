from src.models.user_model import UserModel

class UserRepository:
    def save(self, user):
        user.save()

    def find_by_email(self, email: str):
        return UserModel.objects(email=email).first()

    def find_by_id(self, user_id: str):
        return UserModel.objects(id=user_id).first()

    def create(self, user_data):
        # Converte o DTO em dicionário usando __dict__
        user_dict = user_data.__dict__
        
        # Cria uma instância do modelo com os dados convertidos
        user = UserModel(**user_dict)
        
        # Salva o usuário no MongoDB
        user.save()
        return user

