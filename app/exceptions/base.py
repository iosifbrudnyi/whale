

from typing import Union
from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from fastapi import HTTPException


class ServiceException(Exception):
    pass

class APIException(HTTPException):
    def __init__(self, e: Exception, status_code: int = 400, headers: Union[ Dict[str, str], None ] = None) -> None:
        detail = {"error": str(e)}
        super().__init__(status_code, detail, headers)