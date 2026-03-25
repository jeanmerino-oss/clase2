from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def saludar():
    return {"mensaje": "¡Hola! Bienvenido a mi API"}

@app.get("/bienvenido/{nombre}")
def saludar_persona(nombre: str):
    return {"mensaje": f"Hola {nombre}, ¡qué bueno verte por aquí!"}


servicios_db = [
    {"nombre": "consulta", "precio": 50},
    {"nombre": "baño", "precio": 60},
    {"nombre": "corte", "precio": 100}
]

@app.get("/servicios")
def listar_servicios():
    return {
        "servicios": servicios_db
    }

class Servicio(BaseModel):
    nombre: str
    precio: float

@app.post("/agregar-servicio")
def agregar_servicio(nuevo: Servicio):
    servicios_db.append(nuevo.model_dump())
    return {
        "mensaje": "¡Servicio guardado!"
    }
