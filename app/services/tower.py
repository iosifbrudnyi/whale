
import httpx
from exceptions.base import ServiceException
from config import TOWER_PASS_CREATOR_TOKEN, TOWER_PASS_CREATOR_URL


class TowerService:
    def __init__(self):
        self.url = TOWER_PASS_CREATOR_URL
        self.token = TOWER_PASS_CREATOR_TOKEN


    async def create_pass(self, first_name: str, second_name: str, patronymic: str):
        if self.url == None or self.token == None:
            raise ServiceException("TOWER TOKENS NOT PROVIDED")

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-ACCESS-TOKEN": self.token,
        }

        async with httpx.AsyncClient() as client:
            res = await client.post(
                url=self.url,
                json={
                    "first_name": first_name,
                    "second_name": second_name,
                    "patronymic": patronymic,
                },
                headers=headers,
            )

        return res