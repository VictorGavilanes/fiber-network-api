from fastapi import FastAPI
from routers.nodos import router

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

app.include_router(router)