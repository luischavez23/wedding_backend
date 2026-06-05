from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.rsvp import router as rsvp_router

from app.config.settings import FRONTEND_URL


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=86400,  # 24 horas
)

# Rutas
app.include_router(
    rsvp_router,
    prefix="/api"
)