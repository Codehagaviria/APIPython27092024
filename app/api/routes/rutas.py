from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDtoPeticion, usuarioDtoRespuesta
from app.api.schemas.DTO import GastosDtoPeticion, gastosDtoRespuesta
from app.api.schemas.DTO import CategoriaDtoPeticion, categoriaDtoRespuesta
from app.api.schemas.DTO import MetodoPagoDtoPeticion, MetodoPagoDtoRespuesta
from app.api.models.modelosApp import Usuario
from app.api.models.modelosApp import Gastos
from app.api.models.modelosApp import Categoria
from app.api.models.modelosApp import MetodoPago
from app.database.configuration import sessionLocal, engine

#Para que una api funcione debe tener un archivo enrutador

rutas=APIRouter() #ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite 
#conexion hacia la base de datos

def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback() 
        raise error   
    finally:
        basedatos.close()

#PROGRAMACION DE CADA UNO DE LOS SERVICIOS 
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
#Anotacion:
@rutas.post("/usuarios",response_model=usuarioDtoRespuesta)
def guardarUsuario(datosPeticion:UsuarioDtoPeticion,database:Session=Depends(getDataBase)):
    try:
        usuario=Usuario(
           nombres=datosPeticion.nombre,
           edad=datosPeticion.edad,
           telefono=datosPeticion.telefono,
           correo=datosPeticion.correo,
           contraseña=datosPeticion.contraseña,
           fechaRegistro=datosPeticion.fechaRegistro,
           ciudad=datosPeticion.ciudad
        )
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return usuario
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400,detail="Error al registrar el usuario")
    
@rutas.post("/gastos", response_model=gastosDtoRespuesta)
def guardarGastos(datosPeticion:GastosDtoPeticion,database:Session=Depends(getDataBase)):
    try:
        gasto=Gastos(
           monto=datosPeticion.monto,
           fecha=datosPeticion.fecha,
           descripcion=datosPeticion.descripcion,
           nombre=datosPeticion.nombre
        )
        database.add(gasto)
        database.commit()
        database.refresh(gasto)
        return gasto
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar los Gastos")
    
@rutas.post("/categorias", response_model=categoriaDtoRespuesta)
def guardarCategoria(datosPeticion:CategoriaDtoPeticion,database:Session=Depends(getDataBase)):
    try:
        categoria=Categoria(
           nombrecategoria=datosPeticion.nombrecategoria,
           descripcion=datosPeticion.descripcion,
           fotoicono=datosPeticion.fotoicono        
        )
        database.add(categoria)
        database.commit()
        database.refresh(categoria)
        return categoria
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar la categoria")
    
@rutas.post("/metodopago",response_model=MetodoPagoDtoRespuesta)
def guardarMetodoPago(datosPeticion:MetodoPagoDtoPeticion,database:Session=Depends(getDataBase)):
    try:
        metodopago=MetodoPago(
           nombremetodo=datosPeticion.nombremetodo, 
           descripcion=datosPeticion.descripcion
        )
        database.add(metodopago)
        database.commit()
        database.refresh(metodopago)
        return metodopago
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el Metodo de pago")

@rutas.get("/usuarios",response_model=List[usuarioDtoRespuesta])

def buscarUsuarios(database:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=database.query(Usuario).all()
        return listadoDeUsuarios
    except Exception as error:
        database.rollback()
        raise HTTPException()                 #SE LE COLOCA MENSAJE DE ERROR AL BUSCAR USUARIO?????
    
@rutas.get("/gastos",response_model=List[gastosDtoRespuesta])
def buscarGastos(database:Session=Depends(getDataBase)):
    try:
        listadoDeGastos=database.query(Gastos).all()
        return listadoDeGastos
    except Exception as error:
        database.rollback()
        raise HTTPException()

@rutas.get("/categorias",response_model=List[categoriaDtoRespuesta])
def buscarCategorias(database:Session=Depends(getDataBase)):
    try:
        listadoDeCategorias=database.query(Categoria).all()
        return listadoDeCategorias
    except Exception as error:
        database.rollback()
        raise HTTPException()

@rutas.get("/metodopago",response_model=List[MetodoPagoDtoRespuesta])
def buscarMetodoPago(database:Session=Depends(getDataBase)):
    try:
        listadoDeMetodosPago=database.query(MetodoPago).all()
        return listadoDeMetodosPago
    except Exception as error:
        database.rollback()
        raise HTTPException()









