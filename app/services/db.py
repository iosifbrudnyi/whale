

from typing import List
import datetime
import aiopg
from schemas.leads import LeadBase


class DbService:
    def __init__(self, db_cursor: aiopg.Cursor):
        self.db_cursor = db_cursor

    async def get_fetchall_dict(self, cursor):
        columns = [desc[0] for desc in cursor.description]
        rows = await cursor.fetchall()

        result = []
        for row in rows:
            row_dict = {columns[i]: row[i] for i in range(len(columns))}
            result.append(row_dict)

        return result

    async def client_kit_check_real_type(self, lead: LeadBase):
        """
        Проверка:
            1) По схожим кошелькам в lead_table
            2) По наличию [ tg | mail | phone ] в clients_table
        """
        if lead.wallet != "None" and lead.wallet is not None and len(lead.wallet) > 5:
            await self.db_cursor.execute(
                """
                select *
                from lead_table
                where wallet=%(wallet)s
                """,
                {
                    "wallet": lead.wallet
                }
            )

            resp = await self.db_cursor.fetchone()

            # Если есть данные
            if resp is not None:
                return True

        return False

    async def client_kit_check(self, lead: LeadBase):
        query = "select * from check_lead(%(lead_name)s);"
        await self.db_cursor.execute(query, {"lead_name": lead.lead_name})
        data = self.db_cursor.fetchone()[0]

        if data == "Повторный":  # существует
            return True

        return False

    async def get_request_number_by_lead_name(self, lead_name: str) -> str:
        cursor = self.db.cursor()

        query = f"""
            select count(*)
            from lead_table
            where id = any ((select find_leads_by_name('{lead_name}'))::integer[]) and form_type = 'Китовая'
            and swap_conducted_at is not null;
        """

        await cursor.execute(query)

        count = cursor.fetchone()

        await cursor.close()

        return count[0]

    async def write_lead(self, lead: LeadBase):
        query = """INSERT INTO lead_table(
                        lead_name,
                        meet_time,
                        account,
                        direction,
                        city,
                        statuses,
                        place,
                        description,
                        fiat_amount,
                        crypto_amount,
                        percent,
                        exchange_rate,
                        exchageType,
                        wallet,
                        card_number,
                        platform,
                        billColor
                        )
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        args = (
            str(lead.lead_name),
            str(lead.meet_time),
            str(lead.account),
            str(lead.direction),
            str(lead.city),
            str(lead.statuses),
            str(lead.place),
            str(lead.description),
            str(lead.fiat_amount),
            str(lead.crypto_amount),
            str(lead.percent),
            str(lead.exchange_rate),
            str(lead.exchageType),
            str(lead.wallet),
            str(lead.card_number),
            str(lead.platform),
            str(lead.billColor),
        )
        await self.db_cursor.execute(query, args)

    async def fetch_lead_names(self) -> List[dict]:
        await self.db_cursor.execute(
            "SELECT DISTINCT(name) FROM clients_table"
        ) 

        data = await self.get_fetchall_dict(self.db_cursor)
        return data 

    async def fetch_origin_name(self) -> List[dict]:
        await self.db_cursor.execute("SELECT lead_origin_name FROM lead_origins")
        data = self.db_cursor.fetchall()
        return data  

    async def fetch_meet_time(self) -> List[float]:
        cursor = self.db.cursor()  # buffered=True, dictionary=True)
        cursor.execute(
            "SELECT DISTINCT(meet_time) FROM lead_table where form_type='Китовая'"
        )
        data = cursor.fetchall()
        data = self.posgre_data_with_field_names(data, ["meet_time"])
        time_list = []
        for el in data:
            if el["meet_time"] is None:
                continue
            datetime_object: datetime = el["meet_time"]
            time_list.append(datetime_object.timestamp())
        return time_list

    async def is_lead_exists(self, lead_name: str) -> bool:
        cursor = self.db.cursor()  
        await cursor.execute(f"SELECT * FROM lead_table where lead_name = '{lead_name}'")
        data = cursor.fetchall()
        if data and len(data) != 0:
            return True
        return False

    async def get_today_leads(self) -> int:
        cursor = self.db.cursor()
        await cursor.execute(
            f"SELECT count(id) FROM lead_table WHERE date(create_time) = now()::date;"
        )
        data = cursor.fetchall()
        cursor.close()
        return data[0][0]

    async def get_lead_count_by_request_id(self, request_id: str) -> int:
        cursor = self.db.cursor() 
        await cursor.execute(
            f"SELECT count(id) FROM lead_table WHERE request_id = '{request_id}';"
        )
        data = cursor.fetchall()
        await cursor.close()
        return data[0][0]