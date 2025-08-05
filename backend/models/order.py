from sqlalchemy import Column, String, Integer, Float, ForeignKey
from db import Base


class Order(Base):
    __tablename__ = "pedidos"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    # itens = Column()
    
    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    