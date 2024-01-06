
import hmac
import logging
import httpx
from exceptions.base import ServiceException
from config import CRM_API_URL, CRM_WEBHOOK_KEY
from schemas.leads import LeadBase

class CrmService:

    def __init__(self):
        self.crm_url = CRM_API_URL
        self.secret_webhook_key = CRM_WEBHOOK_KEY

    async def gen_hmac(self, body: dict) -> str:
        """this method generates hmac hash string from request body"""
        byte_message = str(body)
        hmac_hash = hmac.new(
            key=self.secret_webhook_key.encode(),
            msg=byte_message.encode(encoding="UTF-8"),
            digestmod="sha256",
        ).hexdigest()
        return hmac_hash

    async def create_buy_webhook(self, lead_command: dict):
        token = self.gen_hmac(body=lead_command)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

        async with httpx.AsyncClient() as client:
            r = client.post(url=f"{self.crm_url}/webhooks/buyers", json=lead_command, headers=headers)
            
        return r

    async def webhook_command(self, lead: LeadBase, fiat_currencies):
        if self.crm_url == None or self.secret_webhook_key == None:
            raise ServiceException("CRM TOKENS NOT PROVIDED")

        fiat_currency_name, crypto_currency_name = lead["direction"].split(" -> ")

        lead_command = {
            "buyer_name": lead["lead_name"],
            "cash_sum": lead["fiat_amount"].replace(" ", "").replace("-", "0")
            if lead["fiat_amount"]
            else "0",
            "converter_crypto_sum": lead["crypto_amount"]
            .replace(" ", "")
            .replace("-", "0")
            if lead["crypto_amount"]
            else "0",
            "crypto_currency_converter_name": crypto_currency_name,
            "buyer_city_name": lead["city"],
            "buyer_application_num": lead["request_id"],
            "fiat_currency_name": fiat_currency_name,
            "crypto_currency_name": "USDT",
            "client_account": lead["account"],
            "wallet": lead.get("wallet"),
            "fio": lead.get("fio"),
            "lead_origin_name": lead.get("site")
        }

        if fiat_currency_name in fiat_currencies:
            res = self.create_buy_webhook(lead_command=lead_command)
            if not res:
                logging.error("При отправке post-запроса что-то пошло не так")


