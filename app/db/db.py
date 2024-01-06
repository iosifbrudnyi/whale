
from typing import AsyncIterator
import aiopg
from config import POSTGRES_DSN


async def get_db_cursor() -> AsyncIterator:
    async with aiopg.create_pool(dsn=POSTGRES_DSN) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                yield cur