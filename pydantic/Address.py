from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    pinCode: str
    emergency: str | None = None 
