def generate_rsvp_template(name, attend, message):

    attend_text = (
        "✅ Sí asistirá"
        if attend == "si"
        else "❌ No podrá asistir"
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body style="
        margin:0;
        padding:0;
        background:#0A0A0A;
        font-family:Arial, Helvetica, sans-serif;
    ">

        <table
            width="100%"
            cellpadding="0"
            cellspacing="0"
            style="
                background:#0A0A0A;
                padding:20px 10px;
            "
        >
            <tr>
                <td align="center">

                    <table
                        width="100%"
                        cellpadding="0"
                        cellspacing="0"
                        style="
                            max-width:600px;
                            background:#161616;
                            border-top:4px solid #C5A059;
                            color:#FFFFFF;
                        "
                    >

                        <tr>
                            <td style="padding:30px 25px;">

                                <h1 style="
                                    margin:0 0 30px;
                                    color:#C5A059;
                                    text-align:center;
                                    font-size:30px;
                                    font-weight:normal;
                                    font-style:italic;
                                    line-height:1.3;
                                ">
                                    Nueva Confirmación RSVP
                                </h1>

                                <p style="
                                    margin:0 0 15px;
                                    font-size:16px;
                                    line-height:1.6;
                                ">
                                    <strong>Invitado:</strong><br>
                                    {name}
                                </p>

                                <p style="
                                    margin:0 0 15px;
                                    font-size:16px;
                                    line-height:1.6;
                                ">
                                    <strong>Asistencia:</strong><br>
                                    {attend_text}
                                </p>

                                <p style="
                                    margin:0 0 10px;
                                    font-size:16px;
                                ">
                                    <strong>Mensaje:</strong>
                                </p>

                                <div style="
                                    background:#0A0A0A;
                                    padding:20px;
                                    border-left:4px solid #C5A059;
                                    line-height:1.7;
                                    word-break:break-word;
                                ">
                                    {message or "Sin mensaje"}
                                </div>

                                <div style="
                                    margin-top:35px;
                                    padding-top:25px;
                                    border-top:1px solid #2A2A2A;
                                    text-align:center;
                                    color:#C5A059;
                                    font-size:18px;
                                ">
                                    Guadalupe & Eduardo 💍
                                </div>

                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>

    </body>
    </html>
    """