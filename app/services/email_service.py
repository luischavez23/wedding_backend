import requests

from app.config.settings import RESEND_API_KEY, FROM_EMAIL, HTTP_RESEND, EMAIL_TO_1, EMAIL_TO_2, EMAIL_TO_3
from app.templates.rsvp_template import generate_rsvp_template


def send_rsvp_email(name, attend, message):

    html_content = generate_rsvp_template(
        name,
        attend,
        message
    )

    response = requests.post(
        HTTP_RESEND,
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "from": FROM_EMAIL,
            "to": [EMAIL_TO_1, EMAIL_TO_2, EMAIL_TO_3],
            "subject": f"Nueva confirmación de {name}",
            "html": html_content,
        },
    )

    return response