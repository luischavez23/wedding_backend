import requests

from app.config.settings import (
    RESEND_API_KEY,
    FROM_EMAIL,
    HTTP_RESEND,
    EMAIL_TO_1,
    EMAIL_TO_2,
)

from app.templates.rsvp_template import generate_rsvp_template


def send_rsvp_email(name, attend, message):

    html_content = generate_rsvp_template(name, attend, message)

    # 🔥 1. Construir lista de correos correctamente
    emails = [
        EMAIL_TO_1, EMAIL_TO_2,
    ]

    # 🔥 2. Limpiar valores inválidos (None, "", espacios)
    emails = [email.strip() for email in emails if email and email.strip()]

    print("📩 Emails finales:", emails)

    # 🔥 3. Validación crítica
    if not emails:
        print("❌ No hay emails configurados")
        return None

    # 🔥 4. Request a Resend
    response = requests.post(
        HTTP_RESEND,
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "from": FROM_EMAIL,
            "to": emails,
            "subject": f"Nueva confirmación de {name}",
            "html": html_content,
        },
        timeout=10, #10 segundos para evitar bloqueos largos
    )

    # 🔥 5. Debug real (ESTO ES CLAVE)
    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    return response