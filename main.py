from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosApp import Usuario
from app.api.models.modelosApp import Gastos
from app.api.models.modelosApp import Categoria
from app.api.models.modelosApp import MetodoPago
from app.api.routes.rutas import rutas

from starlette.responses import RedirectResponse

#CREAR VARIABLE PARA ADMINISTRAR LAS APLICACION
app=FastAPI()

#ACTIVO EL API
@app.get("/")
def main(): 
    #DOCUMENTAR EL CODIGO
    return RedirectResponse(url="/docs")
app.include_router = (rutas)
