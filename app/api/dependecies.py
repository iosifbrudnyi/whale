

import aiopg
from fastapi import Depends
from services.tg import TgService
from db.db import get_db_cursor
from services.db import DbService
from services.leads import LeadService

def lead_service(db_cursor: aiopg.Cursor = Depends(get_db_cursor)):
    db_service = DbService(db_cursor=db_cursor)
    tg_service = TgService(db_service=db_service)

    lead_service = LeadService(db_service=db_service, tg_service=tg_service)
    return lead_service

