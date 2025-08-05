from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]
    
    class Config:
        from_attributes = True # Configuração para o Python tratar como objeto e não como dicionário