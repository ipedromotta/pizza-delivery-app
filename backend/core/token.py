import os
from http import HTTPStatus
from datetime import datetime, timezone, timedelta

from dotenv import load_dotenv
from jose import jwt, JWTError
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from db.session import Session
from models.user import User


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")


def create_token(id_usuario: int, duracao: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao
    
    dict_info = {
        "sub": str(id_usuario),
        "exp": data_expiracao
    }
    
    encoded_jwt = jwt.encode(dict_info, SECRET_KEY)
    
    return encoded_jwt


def check_token(token: str = Depends(oauth2_schema)) -> User:
    try:
        dict_info = jwt.decode(token, SECRET_KEY)
        id_usuario = int(dict_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Acesso Negado. Verifique a validade do token")
        
    with Session.get_session() as session:
        usuario = session.query(User).filter(User.id == id_usuario).first()
        
        if not usuario:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Acesso Inválido")
        
        return usuario
        