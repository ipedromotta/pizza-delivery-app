from fastapi import APIRouter
from schemas import OrderSchema
from models import Order
from db import Session


order_router = APIRouter(prefix="/orders", tags=["orders"])


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
    