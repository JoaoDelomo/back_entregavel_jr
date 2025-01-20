from repositories.user_repository import UserRepository

class RegisterUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, register_dto):
        # Lógica de validação (se necessário)
        self.user_repository.create(register_dto)
        return {"status": "success", "message": "Usuário registrado com sucesso"}
