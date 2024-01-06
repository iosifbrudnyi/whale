

import datetime
from typing import List

from services.crm import CrmService
from services.tg import TgService
from config import ACCOUNTS, CITIES, CRYPTO_CURRUNCIES, FIAT_CURRENCIES, LEAD_TYPE, PLACES, STATUS_BUY, STATUS_SELL
from schemas.helpers import Direction
from helpers.directions import ExchangeTypeName
from helpers.time_manager import fetch_day_times
from schemas.leads import Account, LeadBase

from services.db import DbService


class LeadService:
  
    def __init__(self, db_service: DbService, tg_service: TgService, crm_service: CrmService = CrmService()):
        self.db_service = db_service
        self.tg_service = tg_service
        self.crm_service = crm_service

        self.account_list = ACCOUNTS
        self.lead_type = LEAD_TYPE
        self.status_sell = STATUS_SELL
        self.status_buy = STATUS_BUY
        self.cities = CITIES
        self.places = PLACES
        self.fiat_currencies = FIAT_CURRENCIES
        self.crypto_currencies = CRYPTO_CURRUNCIES
        self.direction_list = self.combine_directions()

    def combine_directions(self) -> List[Direction]:

        result: List[Direction] = []

        for f in self.fiat_currencies:
            for c in self.crypto_currencies:
                result.append(
                    {
                        "vector": f"{f} -> {c}",
                        "exchange_type": ExchangeTypeName.BUY.value
                    }
                )
                result.append(
                    {
                        "vector": f"{c} -> {f}",
                        "exchange_type": ExchangeTypeName.SELL.value
                    }
                )

        result.sort(key=lambda x: x['vector'])

        return result

    def get_accounts(self) -> List[Account]:
        return [{"name": account} for account in self.account_list]

    def get_direction(self) -> List[Direction]:
        return self.direction_list

    async def get_lead_names(self) -> List[str]:
        leads = await self.db_service.fetch_lead_names()
        lead_names = []
        for el in leads:
            lead_names.append(el["name"])
        return lead_names

    def get_status_buy(self) -> List[str]:
        return self.status_buy

    def get_status_sell(self) -> List[str]:
        return self.status_sell

    def get_cities(self) -> List[str]:
        return self.cities

    def get_places(self) -> List[str]:
        return self.places

    def get_free_time(self) -> List[datetime.datetime]:
        possible = fetch_day_times()
        return possible

    async def lead_create_buy(self, lead: LeadBase):
        await self.db_service.write_lead(lead=lead)
        await self.tg_service.chat_inform(lead=lead)  
        await self.crm_service.webhook_command(lead=lead)
        
        return lead
    
    async def lead_create_sell(self, lead: LeadBase):
        lead.statuses = [] + lead.statuses
        await self.db_service.write_lead(lead=lead)

  
