from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException

from db import Session
from core import check_token
from models import Order, User, Item
from schemas import OrderSchema, ItemSchema


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
        
@order_router.get("/list")
async def list_orders(usuario: User = Depends(check_token)):
    if usuario.admin == False:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Você não tem autorização para fazer essa operação")
        
    with Session.get_session() as session:
        pedidos = session.query(Order).all()
        
        return {
            "orders": pedidos
        }
        
@order_router.post("/add-item/{id_pedido}")        
async def add_item(id_pedido: int, item_schema: ItemSchema, usuario: User = Depends(check_token)):
    with Session.get_session() as session:
        pedido = session.query(Order).filter(Order.id == id_pedido).first()
        
        if not pedido:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Pedido não existe")
         
        if not usuario.admin and usuario.id != pedido.id:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Você não tem autorização para fazer essa operação")
        
        item = Item(
            item_schema.quantidade,
            item_schema.sabor,
            item_schema.tamanho,
            item_schema.preco_unitario,
            id_pedido
        )
        
        session.add(item)
        pedido.calculate_price()
        session.commit()
        
        return {
            "message": "Item criado com sucesso",
            "item_id": item.id,
            "order_price": pedido.preco
        }
        