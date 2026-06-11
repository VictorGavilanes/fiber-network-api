from pydantic import BaseModel


class Nodo(BaseModel):
    id: int
    nombre: str
    ciudad: str