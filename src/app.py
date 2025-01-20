from fastapi import FastAPI
from mongoengine import connect, get_db
from fastapi.middleware.cors import CORSMiddleware
import os
import glob
import dotenv
from importlib import import_module
import os
import sys

# Adiciona o diretório src ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


try:
    db = get_db()
    print(f"Conectado ao banco de dados: {db.name}")
except Exception as e:
    print(f"Erro na conexão com o MongoDB: {e}")



dotenv.load_dotenv()


dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../.env'))

connect(
    db="entregavel",  # Nome do banco de dados
    host=f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PWD')}@{os.getenv('MONGO_CLUSTER')}/?retryWrites=true&w=majority",
    alias="default"
)

# Instanciação do FastAPI
app = FastAPI()

# Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # URL do front-end permitido (ajuste conforme sua configuração)
    allow_credentials=True,                   # Permitir cookies ou headers de autenticação
    allow_methods=["*"],                      # Permitir todos os métodos HTTP
    allow_headers=["*"],                      # Permitir todos os headers
)



# Diretório atual onde o arquivo app.py está localizado
working_directory = os.path.dirname(os.path.abspath(__file__))

# Diretório onde os "use_cases" estão localizados
use_cases_directory = os.path.join(working_directory, "use_cases")

# Procura recursivamente por arquivos index.py nos diretórios de casos de uso
routes = glob.glob(os.path.join(use_cases_directory, "**/index.py"), recursive=True)

# Importa e registra automaticamente as rotas definidas em cada arquivo index.py
for route in routes:
    # Converte o caminho do arquivo em um nome de módulo relativo
    relative_path = os.path.relpath(route, working_directory)
    module_name = os.path.splitext(relative_path)[0].replace(os.path.sep, '.')
    try:
        # Importa dinamicamente o módulo
        module = import_module(module_name)
        # Se o módulo possui um objeto 'router', inclui as rotas no aplicativo FastAPI
        if hasattr(module, 'router'):
            app.include_router(module.router)
    except ModuleNotFoundError as e:
        print(f"Erro ao importar módulo {module_name}: {e}")

