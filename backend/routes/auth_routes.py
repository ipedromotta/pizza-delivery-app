from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from db import Session
from models import User
from core import Criptografia
from schemas import UserSchema


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def home():
    return {"message": "teste", "is_authenticated": False}

@auth_router.post("/register")
def register_user(usuario_schema: UserSchema):
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
        
    