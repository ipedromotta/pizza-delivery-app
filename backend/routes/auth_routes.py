
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from db import Session
from models import User
from http import HTTPStatus
from core import Criptografia
from core import check_token, create_token
from schemas import UserSchema, LoginSchema


auth_router = APIRouter(prefix="/auth", tags=["auth"])


def auth_user(email: str, senha: str):
    with Session.get_session() as session:
        usuario = session.query(User).filter(User.email == email).first()
        
        if usuario and Criptografia.verificar_senha(senha, usuario.senha):
            return usuario
        
        else:
            return False


@auth_router.get("/")
async def home():
    return {"message": "teste", "is_authenticated": False}

@auth_router.post("/register")
async def register_user(usuario_schema: UserSchema):
    with Session.get_session() as session:
        usuario = session.query(User).filter(User.email == usuario_schema.email).first()
        
        if usuario:
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Email de usuário já cadastrado")
        
        else:
            senha_criptografada = Criptografia.criptografar(usuario_schema.senha)
            novo_usuario = User(
                nome=usuario_schema.nome,
                email=usuario_schema.email,
                senha=senha_criptografada,
                ativo=usuario_schema.ativo,
                admin=usuario_schema.admin
                )
            session.add(novo_usuario)
            session.commit()
            return {"message": f"Usuário criado com sucesso! {usuario_schema.email}"}
        
@auth_router.post("/login")    
async def login(login_schema: LoginSchema):
    usuario = auth_user(
        login_schema.email,
        login_schema.senha
    )

    if not usuario:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado ou credenciais inválidas")
    
    else:
        access_token = create_token(usuario.id)
        refresh_token = create_token(usuario.id, duracao=timedelta(days=7))
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }
        
@auth_router.post("/login-form")
async def login_form(formulario_login: OAuth2PasswordRequestForm = Depends()):
    usuario = auth_user(
        formulario_login.username,
        formulario_login.password
    )

    if not usuario:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado ou credenciais inválidas")
    
    else:
        access_token = create_token(usuario.id)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }

@auth_router.get("/refresh")
async def user_refresh_token(usuario: User = Depends(check_token)):
    access_token = create_token(usuario.id)

    return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
