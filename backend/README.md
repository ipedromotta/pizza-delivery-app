## 📦 Migrações de Banco de Dados com Alembic
Este projeto utiliza o Alembic para gerenciar migrações do banco de dados.

### 🔧 Inicializar Alembic no projeto
⚠️ Só use este comando se o projeto ainda não tiver a pasta do Alembic configurada.
```
alembic init alembic
```
### 🛠️ Criar uma migração (criação ou alteração no banco)
- Certifique-se de configurar corretamente a **SQLALCHEMY_DATABASE_URL** no **alembic.ini** ou no arquivo **env.py**.

```
alembic revision --autogenerate -m "criação da estrutura inicial"
```
- Esse comando detecta automaticamente mudanças no modelo do banco de dados (como criação/remoção de colunas ou tabelas) e gera um arquivo de migração correspondente.
- ✅ As alterações são aplicadas sem perder os dados existentes, desde que a mudança seja compatível (ex: adicionar uma nova coluna é seguro; excluir uma coluna apagará seus dados, naturalmente).
### 🚀 Aplicar as migrações
```
alembic upgrade head
```