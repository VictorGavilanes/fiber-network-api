from models.nodo import Nodo
from data.database import conexion, cursor
from fastapi import APIRouter, HTTPException
import sqlite3

router = APIRouter()

@router.post("/nodos")
def crear_nodo_db(nodo: Nodo):

    try:

        cursor.execute(
            """
            INSERT INTO nodos (id, nombre, ciudad)
            VALUES (?, ?, ?)
            """,
            (
                nodo.id,
                nodo.nombre,
                nodo.ciudad
            )
        )

        conexion.commit()

        return {
            "mensaje": "Nodo agregado correctamente",
            "nodo": nodo
        }

    except sqlite3.IntegrityError:

        raise HTTPException(
            status_code=400,
            detail="El ID ya existe"
        )

@router.get("/nodos-db/{id}")
def obtener_nodo_db(id: int):

    cursor.execute("""
        SELECT id, nombre, ciudad
        FROM nodos
        WHERE id = ?
    """, (id,))

    resultado = cursor.fetchone()

    if resultado is None:
     raise HTTPException(
        status_code=404,
        detail="Nodo no encontrado")

    return {
        "id": resultado[0],
        "nombre": resultado[1],
        "ciudad": resultado[2]
    }

@router.put("/nodos-db/{id}")
def actualizar_nodo_db(id: int, nodo: Nodo):

    cursor.execute("""
        UPDATE nodos
        SET nombre = ?, ciudad = ?
        WHERE id = ?
    """,
    (
        nodo.nombre,
        nodo.ciudad,
        id
    ))

    conexion.commit()

    if cursor.rowcount == 0:
     raise HTTPException(
        status_code=404,
        detail="Nodo no encontrado"
    )

    return {
        "mensaje": "Nodo actualizado correctamente"
    }

@router.delete("/nodos-db/{id}")
def eliminar_nodo_db(id: int):

    cursor.execute("""
        DELETE FROM nodos
        WHERE id = ?
    """, (id,))

    conexion.commit()

    if cursor.rowcount == 0:
      raise HTTPException(
        status_code=404,
        detail="Nodo no encontrado"
    )

    return {
        "mensaje": "Nodo eliminado correctamente"
    }

@router.get("/nodos")
def obtener_nodos():

    cursor.execute("""
        SELECT id, nombre, ciudad
        FROM nodos
    """)

    resultados = cursor.fetchall()

    nodos = []

    for fila in resultados:
        nodos.append({
            "id": fila[0],
            "nombre": fila[1],
            "ciudad": fila[2]
        })

    return nodos