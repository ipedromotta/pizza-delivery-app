# ⚙️ Configuração do projeto #

## 🖥️ Execução local

### ⚙️ 1. Ativar ambiente virtual com uv

Se você ainda não possui o **uv**, instale-o:

```sh
pip install uv
```

---

### 📦 2. Instalar dependências

No diretório `backend`, crie o ambiente virtual e instale tudo que o projeto precisa:

```sh
cd backend
uv venv
uv pip install -r requirements.txt
```

---

### 🧬 3. Migrações de Banco de Dados com Alembic

Este projeto utiliza **Alembic** para gerenciar as migrações do banco de dados (via SQLAlchemy).

> 💡 **Onde o Alembic entra no fluxo?**
> Utilize-o **após instalar as dependências** e **antes de subir o servidor**, especialmente quando houver alterações nos modelos SQLAlchemy.

## 🔧 Inicializar Alembic (apenas uma vez)

Se o projeto ainda não possui a pasta `alembic/`:

```sh
alembic init alembic
```

## 🛠️ Criar uma nova migração

Configure o `SQLALCHEMY_DATABASE_URL` no `alembic.ini` ou no `env.py` e execute:

```sh
alembic revision --autogenerate -m "criação da estrutura inicial"
```

* Detecta mudanças automaticamente no modelo.
* Mantém os dados existentes, exceto em alterações destrutivas.

## 🚀 Aplicar as migrações

```sh
alembic upgrade head
```

---

### ▶️ 4. Subir o servidor FastAPI

Após aplicar as migrações, execute o servidor local:

```sh
uv run uvicorn app.main:app --reload
```

Ou conforme o nome correto do módulo da sua aplicação.

A API ficará disponível em:
🔗 **[http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)**

Documentação automática:

* Swagger UI: 🔗 **[http://localhost:8000/docs](http://localhost:8000/docs)**
* ReDoc: 🔗 **[http://localhost:8000/redoc](http://localhost:8000/redoc)**

---
