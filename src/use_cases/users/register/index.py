from fastapi import APIRouter
from src.use_cases.users.register.register_use_case import RegisterUseCase
from src.repositories.user_repository import UserRepository
from src.use_cases.users.register.register_dto import RegisterDTO

router = APIRouter()

user_repository = UserRepository()
register_use_case = RegisterUseCase(user_repository)

@router.post("/users/register")
def register_user(register_dto: RegisterDTO):
    return register_use_case.execute(register_dto)
