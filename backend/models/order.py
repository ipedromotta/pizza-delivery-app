from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Order(Base):
    __tablename__ = "pedidos"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    itens = relationship("Item", cascade="all, delete")
    
    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    
    def calculate_price(self):
        self.preco = sum(item.preco_unitario * item.quantidade for item in self.itens)
    