from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.rsvp import router as rsvp_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(
    rsvp_router,
    prefix="/api"
)