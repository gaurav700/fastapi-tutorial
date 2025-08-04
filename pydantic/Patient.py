from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import List, Dict
from Address import Address

# Creating pydantic base model
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height : int
    allergies: List[str]
    contact: Address

    @computed_field
    @property
    def calcuate_bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if  model.age > 60 and 'emergency' not in model.contact:
            raise ValueError('Emergency contact is required for senior citizens')
        return model

    @field_validator('email', mode='before')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Invalid email domain')
        return value
