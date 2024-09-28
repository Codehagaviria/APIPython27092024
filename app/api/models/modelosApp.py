from sqlalchemy import Column,Integer, String, Float, Date          #Atributos tipo de datos
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la Aplicacion
#Modelo USUARIO
class Usuario(Base):
    __tablename__='usuarios'            #crea una tabla le coloca el nombre usuario
    id=Column(Integer, primary_key=True,autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))


#Modelo GASTOS
class Gastos(Base):
    __tablename__='gastos'
    id=Column(Integer, primary_key=True,autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(50))
    nombre=Column(String(50))

#Modelo CATEGORIA
class Categoria(Base):
    __tablename__='categoria'
    id=Column(Integer, primary_key=True,autoincrement=True)
    nombreCategoria=Column(String(50))                 #comida, transporte, entretenimiento
    descripcion=Column(String(50))
    fotoicono=Column(String(100))                       #como es una url el tamaño lo coloco de 100               


#Modelo METODOS DE PAGO
class MetodoPago(Base):
    __tablename__='metodos_de_Pago'
    id=Column(Integer, primary_key=True,autoincrement=True)
    nombreMetodo=Column(String(50)) 
    descripcion=Column(String(50))

#Modelo FACTURA
class Factura(Base):
    pass
