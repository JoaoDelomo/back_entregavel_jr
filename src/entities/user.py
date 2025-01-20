from pydantic import BaseModel
from typing import Literal

class User(BaseModel):
    _id: str
    name: str
    email: str
    password: str
    role: Literal["User", "Admin"]

    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0
