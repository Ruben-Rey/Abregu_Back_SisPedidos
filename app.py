from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.endpoints.pedidos import router as user_router

app = FastAPI()

origins = [
    "http://localhost:5173",  # Origen de tu aplicación React
]

app.include_router(user_router, prefix="/pedidosAll", tags=["pedidosAll"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Puedes especificar los métodos que deseas permitir
    allow_headers=["*"],  # Puedes especificar los encabezados que deseas permitir
)