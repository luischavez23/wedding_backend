from fastapi import APIRouter
from app.models.rsvp_model import RSVP
from app.services.email_service import send_rsvp_email

router = APIRouter()


@router.post("/send-rsvp/")
async def send_rsvp(data: RSVP):

    response = send_rsvp_email(
        data.name,
        data.attend,
        data.message
    )

    if response.status_code != 200:
        return {
            "success": False,
            "error": response.text
        }

    return {
        "success": True,
        "message": "Correo enviado correctamente"
    }