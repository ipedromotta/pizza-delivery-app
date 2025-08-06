from pydantic import BaseModel


class OrderSchema(BaseModel):
    id_usuario: int
    
    class Config:
        from_attributes = True # Configuração para o Python tratar como objeto e não como dicionário
    