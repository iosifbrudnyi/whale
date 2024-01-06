
from pydantic import BaseModel


class PassInfoBase(BaseModel):
    first_name: str 
    second_name: str
    patronymic: str