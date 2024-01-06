from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends
from api.dependecies import lead_service
from exceptions.base import APIException, ServiceException

from schemas.helpers import Direction
from schemas.leads import Account, LeadBase
from services.leads import LeadService

router = APIRouter()

@router.get("/get_accounts")
def get_accounts(lead_service: LeadService = Depends(lead_service)) -> List[Account]:
    return lead_service.get_accounts()


@router.get("/get_direction")
def get_directions(lead_service: LeadService = Depends(lead_service)) -> List[Direction]:
    return lead_service.get_direction()


@router.get("/get_lead_name")
async def get_lead_name(lead_service: LeadService = Depends(lead_service)) -> List[str]:
    return await lead_service.get_lead_names()


@router.get("/get_free_time")
async def get_free_time(lead_service: LeadService = Depends(lead_service)) -> List[datetime]:
    return await lead_service.get_free_time()


@router.get("/get_status_buy")
def get_status_buy(lead_service: LeadService = Depends(lead_service)) -> List[str]:
    return lead_service.get_status_buy()


@router.get("/get_status_sell")
def get_status_sell(lead_service: LeadService = Depends(lead_service)) -> List[str]:
    return lead_service.get_status_sell()

@router.get("/get_cities")
def get_cities(lead_service: LeadService = Depends(lead_service)) -> List[str]:
    return lead_service.get_cities()


@router.get("/get_places")
def get_places(lead_service: LeadService = Depends(lead_service)) -> List[str]:
    return lead_service.get_places()

@router.post("/save_lead_sell")
async def save_lead_sell(lead_sell: LeadBase, lead_service: LeadService = Depends(lead_service)) -> LeadBase:    
    if lead_sell:
        try:
            await lead_service.lead_create_sell(lead=lead_sell)
            return lead_sell
        
        except ServiceException as se:
            raise APIException(se)

        except Exception as e:
            raise APIException(e)

    raise APIException("Bad request")


@router.post("/save_lead_buy")
async def save_lead_buy(lead_buy: LeadBase, lead_service: LeadService = Depends(lead_service)) -> LeadBase:    
    if lead_buy:
        try:
            await lead_service.lead_create_buy(lead=lead_buy)
            return lead_buy
        
        except ServiceException as se:
            raise APIException(se)

        except Exception as e:
            raise APIException(e)
        
    raise APIException("Bad request")
    

