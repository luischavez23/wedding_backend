def generate_rsvp_template(name, attend, message):

    attend_text = (
        "✅ Sí asistirá"
        if attend == "si"
        else "❌ No podrá asistir"
    )

    return f"""
    <div style="
        font-family: Arial, sans-serif;
        background: #0A0A0A;
        padding: 40px;
        color: white;
    ">
        <div style="
            max-width: 600px;
            margin: auto;
            background: #161616;
            padding: 40px;
            border-top: 4px solid #C5A059;
        ">

            <h1 style="
                color: #C5A059;
                text-align: center;
                font-style: italic;
            ">
                Nueva Confirmación RSVP
            </h1>

            <p>
                <strong>Invitado:</strong> {name}
            </p>

            <p>
                <strong>Asistencia:</strong> {attend_text}
            </p>

            <p>
                <strong>Mensaje:</strong>
            </p>

            <div style="
                background: #0A0A0A;
                padding: 20px;
                border-left: 3px solid #C5A059;
            ">
                {message or "Sin mensaje"}
            </div>

            <div style="
                margin-top: 40px;
                text-align: center;
                color: white;
            ">
                Guadalupe & Eduardo 💍
            </div>
        </div>
    </div>
    """