from fastapi import FastAPI

app = FastAPI()

from auth_rota import auth_rotas
from order_rota import order_rotas

app.include_router(auth_rotas)
app.include_router(order_rotas)