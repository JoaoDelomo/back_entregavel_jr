import jwt
from repositories.user_repository import UserRepository
from use_cases.users.login.login_dto import LoginDTO
import os

class LoginUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, login_dto):
        user = self.user_repository.find_by_email(login_dto.email)
        if not user or not user.check_password(login_dto.password):
            raise Exception("Credenciais inválidas")
        
        # Serializa o ObjectId para string
        token = jwt.encode(
            {"id": str(user.id), "email": user.email},
            os.getenv("JWT_SECRET"),
            algorithm="HS256"
        )
        return {"token": token}

