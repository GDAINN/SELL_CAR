from fastapi import APIRouter

order_rotas = APIRouter(prefix="/COMPRA_VENDAS", tags=["ROTAS/API"])

@order_rotas.get("/lista")
async def ver_carros():
    return {"menssagem": "Você acessou a rota lista"}

