from fastapi import APIRouter
from use_cases.users.login.login_use_case import LoginUseCase
from use_cases.users.login.login_dto import LoginDTO
from repositories.user_repository import UserRepository

router = APIRouter()

user_repository = UserRepository()
login_use_case = LoginUseCase(user_repository)

@router.post("/users/login")
def login_user(login_dto: LoginDTO):
    return login_use_case.execute(login_dto)
