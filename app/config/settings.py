import os
from dotenv import load_dotenv

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO=os.getenv("EMAIL_TO")
FROM_EMAIL=os.getenv("FROM_EMAIL")
HTTP_RESEND=os.getenv("HTTP_RESEND")
ENV=os.getenv("ENV", "production")