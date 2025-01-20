from mongoengine import *
from cryptography.fernet import Fernet
import os
import bcrypt
import dotenv

dotenv.load_dotenv()

fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class UserModel(Document):
    meta = {'collection': 'users'}

    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)

    def clean(self):
        """
        Método chamado antes de salvar o documento.
        Verifica se a senha precisa ser hashada.
        """
        if not self.password.startswith("$2b$"):  # Verifica se a senha já está em hash
            self.password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password: str) -> bool:
        """
        Verifica se a senha fornecida coincide com a senha armazenada no banco de dados.
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
