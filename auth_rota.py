from fastapi import APIRouter

auth_rotas = APIRouter(prefix="/Autentificação", tags=["LOGIN/SENHAS"])
@auth_rotas.get("/auth")
async def autentificacao():
    return {"menssagem": "Essa rota está funcionando"}