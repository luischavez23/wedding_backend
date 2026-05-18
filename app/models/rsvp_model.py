from pydantic import BaseModel

class RSVP(BaseModel):
    name: str
    attend: str
    message: str