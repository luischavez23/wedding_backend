import os
from dotenv import load_dotenv

load_dotenv()

FRONTEND_URL=os.getenv("FRONTEND_URL")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO_1=os.getenv("EMAIL_TO_1")
EMAIL_TO_2=os.getenv("EMAIL_TO_2")
EMAIL_TO_3=os.getenv("EMAIL_TO_3")
FROM_EMAIL=os.getenv("FROM_EMAIL")
HTTP_RESEND=os.getenv("HTTP_RESEND")
ENV=os.getenv("ENV", "production")
