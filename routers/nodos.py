from fastapi import APIRouter
from models.nodo import Nodo
from data.nodos import nodos

router = APIRouter()

@router.get("/nodos")
def obtener_nodos():
    return nodos

@router.get("/nodos/{id}")
def obtener_nodo(id: int):

    for nodo in nodos:
        if nodo["id"] == id:
            return nodo

    return {"error": "Nodo no encontrado"}

@router.post("/nodos")
def crear_nodo(nodo: Nodo):

    nodos.append(nodo.model_dump())

    return {
        "mensaje": "Nodo agregado correctamente",
        "nodo": nodo
    }

@router.put("/nodos/{id}")
def actualizar_nodo(id: int, nodo_actualizado: Nodo):

    for index, nodo in enumerate(nodos):

        if nodo["id"] == id:

            nodos[index] = nodo_actualizado.model_dump()

            return {
                "mensaje": "Nodo actualizado correctamente",
                "nodo": nodo_actualizado
            }

    return {"error": "Nodo no encontrado"}

@router.delete("/nodos/{id}")
def eliminar_nodo(id: int):

    for index, nodo in enumerate(nodos):

        if nodo["id"] == id:

            nodo_eliminado = nodos.pop(index)

            return {
                "mensaje": "Nodo eliminado correctamente",
                "nodo": nodo_eliminado
            }

    return {"error": "Nodo no encontrado"}