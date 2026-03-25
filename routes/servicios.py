from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

servicios_db = [
    {"nombre": "consulta", "precio": 50},
    {"nombre": "baño", "precio": 60},
    {"nombre": "corte", "precio": 100}
]

class Servicio(BaseModel):
    nombre: str
    precio: float

@router.get("/servicios")
def listar_servicios():
    return {
        "servicios": servicios_db
    }

@router.post("/agregar-servicio")
def agregar_servicio(nuevo: Servicio):
    servicios_db.append(nuevo.model_dump())
    return {
        "mensaje": "¡Servicio guardado!"
    }
