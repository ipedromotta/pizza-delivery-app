from pydantic import BaseModel


class LoginSchema(BaseModel):
    email: str
    senha: str
    
    class Config:
        from_attributes = True # Configuração aceitar objeto, não apenas dicionário