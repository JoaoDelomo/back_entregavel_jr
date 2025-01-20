
# Backend - API de Gerenciamento de Despesas e Receitas

Este é o backend da aplicação de gerenciamento de despesas e receitas, desenvolvido com **FastAPI** e utilizando o **MongoDB** como banco de dados.

## Funcionalidades

- **Autenticação de Usuário**: Login utilizando token JWT.
- **Gestão de Despesas**: Criar, listar, editar e excluir despesas.
- **Gestão de Receitas**: Criar, listar, editar e excluir receitas.
- **Cálculos e Relatórios**: Permite calcular o total de despesas e receitas.

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno para construção de APIs.
- **MongoDB**: Banco de dados NoSQL utilizado para persistência de dados.
- **Pydantic**: Validação e tipagem dos dados.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/usuario/repo-backend.git
    ```

2. Entre na pasta do projeto:
    ```bash
    cd 
    ```

3. Crie e ative o ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure o MongoDB:
    - Crie uma instância do MongoDB ou conecte-se a um banco de dados existente.
    - Certifique-se de que a conexão esteja funcionando.

6. Rode a aplicação:
    ```bash
    uvicorn src.app:app --reload
    ```

    A API estará disponível em `http://127.0.0.1:8000`.

## EndPoints

### Autenticação
- `POST /users/login`: Realiza o login e retorna um token JWT.

### Despesas
- `POST /expenses`: Cria uma nova despesa.
- `GET /expenses`: Lista todas as despesas.
- `PUT /expenses/{expense_id}`: Atualiza uma despesa.
- `DELETE /expenses/{expense_id}`: Exclui uma despesa.

### Receitas
- `POST /receipts`: Cria uma nova receita.
- `GET /receipts`: Lista todas as receitas.
- `PUT /receipts/{receipt_id}`: Atualiza uma receita.
- `DELETE /receipts/{receipt_id}`: Exclui uma receita.

## Notas
- Certifique-se de que o MongoDB esteja rodando corretamente antes de iniciar a aplicação.
- Para autenticação, utilize o token retornado pelo endpoint de login em todas as requisições subsequentes.
