from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

usuarios_db = []

class Usuario(BaseModel):
    correo: str
    password: str

@router.post("/register")
def register(usuario: Usuario):
    usuarios_db.append(usuario.model_dump())
    return {
        "mensaje": "¡Registro exitoso!",
        "datos": usuario.model_dump()
    }

@router.post("/login")
def login(usuario: Usuario):
    return {
        "mensaje": "¡Login exitoso!",
        "datos": usuario.model_dump()
    }
