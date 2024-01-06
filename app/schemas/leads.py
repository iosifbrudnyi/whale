from typing import Union
from datetime import date
from typing import List
from pydantic import BaseModel, EmailStr


class LeadBase(BaseModel):
    lead_name: str
    account: EmailStr
    meet_time: date
    site: str
    direction: str
    city: str
    statuses: List[str]
    place: Union[str, None]
    description: Union[str, None]
    fiat_amount: Union[str, None]
    crypto_amount: Union[str, None]
    percent: Union[str, None]
    exchange_rate: Union[str, None]
    wallet: Union[str, None]
    card_number: Union[str, None]
    platform: Union[str, None]
    billColor: Union[str, None]
    exchageType: Union[str, None]
    crm_lead_id: Union[str, None]
    is_percent_change: Union[str, None]
    chat_id: str
    fio: str

class Account(BaseModel):
    name: str

