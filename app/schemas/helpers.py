from pydantic import BaseModel


class Direction(BaseModel):
    vector: str
    exchange_type: str