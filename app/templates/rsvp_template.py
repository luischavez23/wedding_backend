def generate_rsvp_template(name, attend, message):

    attend_text = (
        "Sí asistirá a la celebración"
        if attend == "si"
        else "No podrá asistir"
    )

    attend_color = (
        "#C5A059"
        if attend == "si"
        else "#D87A7A"
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
        font-family:Georgia, serif;
    ">

    <table width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <td align="center" style="padding:40px 15px;">

                <table
                    width="100%"
                    cellpadding="0"
                    cellspacing="0"
                    style="
                        max-width:650px;
                        background:#111111;
                        border:1px solid #C5A059;
                    "
                >

                    <!-- Encabezado -->
                    <tr>
                        <td align="center" style="padding:50px 30px 20px;">

                            <div style="
                                color:#C5A059;
                                font-size:14px;
                                letter-spacing:5px;
                                text-transform:uppercase;
                            ">
                                RSVP
                            </div>

                            <div style="
                                margin-top:15px;
                                color:#FFFFFF;
                                font-size:38px;
                                font-style:italic;
                                line-height:1.3;
                            ">
                                Guadalupe & Eduardo
                            </div>

                            <div style="
                                margin-top:18px;
                                color:#C5A059;
                                font-size:20px;
                            ">
                                ✦
                            </div>

                        </td>
                    </tr>

                    <!-- Título -->
                    <tr>
                        <td align="center" style="padding:10px 30px 40px;">

                            <div style="
                                color:#F5F5F5;
                                font-size:22px;
                                letter-spacing:2px;
                                text-transform:uppercase;
                            ">
                                Nueva Confirmación
                            </div>

                        </td>
                    </tr>

                    <!-- Contenido -->
                    <tr>
                        <td style="padding:0 40px;">

                            <table width="100%">

                                <tr>
                                    <td style="
                                        padding:18px 0;
                                        border-bottom:1px solid #2A2A2A;
                                    ">
                                        <div style="
                                            color:#C5A059;
                                            font-size:12px;
                                            letter-spacing:2px;
                                            text-transform:uppercase;
                                        ">
                                            Invitado
                                        </div>

                                        <div style="
                                            color:#FFFFFF;
                                            font-size:22px;
                                            margin-top:8px;
                                        ">
                                            {name}
                                        </div>
                                    </td>
                                </tr>

                                <tr>
                                    <td style="
                                        padding:18px 0;
                                        border-bottom:1px solid #2A2A2A;
                                    ">
                                        <div style="
                                            color:#C5A059;
                                            font-size:12px;
                                            letter-spacing:2px;
                                            text-transform:uppercase;
                                        ">
                                            Confirmación
                                        </div>

                                        <div style="
                                            color:{attend_color};
                                            font-size:20px;
                                            margin-top:8px;
                                        ">
                                            {attend_text}
                                        </div>
                                    </td>
                                </tr>

                            </table>

                        </td>
                    </tr>

                    <!-- Mensaje -->
                    <tr>
                        <td style="padding:35px 40px;">

                            <div style="
                                color:#C5A059;
                                font-size:12px;
                                letter-spacing:2px;
                                text-transform:uppercase;
                                margin-bottom:15px;
                            ">
                                Mensaje
                            </div>

                            <div style="
                                background:#181818;
                                border-left:3px solid #C5A059;
                                padding:25px;
                                color:#E5E5E5;
                                line-height:1.8;
                                font-size:16px;
                                word-break:break-word;
                            ">
                                {message or "El invitado no dejó ningún mensaje."}
                            </div>

                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td align="center" style="
                            padding:30px 40px 50px;
                        ">

                            <div style="
                                width:80px;
                                height:1px;
                                background:#C5A059;
                                margin:auto;
                            ">
                            </div>

                            <div style="
                                margin-top:25px;
                                color:#C5A059;
                                font-size:24px;
                            ">
                                💍
                            </div>

                            <div style="
                                margin-top:15px;
                                color:#FFFFFF;
                                font-size:18px;
                                letter-spacing:1px;
                            ">
                                Guadalupe & Eduardo
                            </div>

                            <div style="
                                margin-top:10px;
                                color:#A5A5A5;
                                font-size:13px;
                            ">
                                Confirmación recibida desde el sitio web
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