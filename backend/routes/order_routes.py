from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException

from db import Session
from core import check_token
from models import Order, User
from schemas import OrderSchema


order_router = APIRouter(prefix="/orders", tags=["orders"], dependencies=[Depends(check_token)])


@order_router.get("/")
async def orders():
    return {"message": "Você acessou a rota de pedidos."}

@order_router.post("/create")
async def create_order(pedido_schema: OrderSchema):
    novo_pedido = Order(usuario=pedido_schema.id_usuario)
    
    with Session.get_session() as session:
        session.add(novo_pedido)
        session.commit()
        
        return {"message": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}
    
@order_router.post("/cancel/{id_pedido}")
async def cancel_order(id_pedido: int, usuario: User = Depends(check_token)):
    with Session.get_session() as session:
        pedido = session.query(Order).filter(Order.id == id_pedido).first()
        
        if not pedido:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Pedido não encontrado")
        
        if not usuario.admin or usuario.id != pedido.usuario:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Você não tem autorização para cancelar esse pedido.")
        
        pedido.status = "CANCELADO"
        session.commit()
        
        return {
            "message": f"Pedido número {pedido.id} cancelado com sucesso",
            "order": pedido
        }