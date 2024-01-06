

from fastapi import APIRouter, Depends
from exceptions.base import APIException, ServiceException

from schemas.tower import PassInfoBase
from services.tower import TowerService


router = APIRouter(prefix="/tower")

@router.post("/create_pass")
async def create_pass(pass_info: PassInfoBase, tower_service: TowerService = Depends(TowerService)):
    try:
        await tower_service.create_pass(**pass_info.model_dump())
    except ServiceException as se:
        raise APIException(se)
    
    return pass_info