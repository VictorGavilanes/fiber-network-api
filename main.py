from fastapi import FastAPI
from routers.nodos import router

app = FastAPI()

app.include_router(router)