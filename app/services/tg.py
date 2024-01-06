
import datetime

import telegram
from exceptions.base import ServiceException
from config import BOT_TOKEN, CHAT_KIT, DUBAI_CHAT_KIT, SPB_CHAT_KIT, TIMEZONE, TURKEY_CHAT_KIT
from schemas.leads import LeadBase
from services.db import DbService


class TgService:
    def __init__(self, db_service: DbService) -> None:
        self.db_service = db_service
        self.tz = TIMEZONE
        self.chat_kit = CHAT_KIT
        self.bot_token = BOT_TOKEN
        self.spb_chat_kit = SPB_CHAT_KIT or 0
        self.dubai_chat_kit = DUBAI_CHAT_KIT or 0
        self.turkey_chat_kit = TURKEY_CHAT_KIT or 0

    def tg_report_filter(self, lead: LeadBase) -> dict:
        d = lead.__dict__
        for i in d:
            if d[i] == "None" or not d[i] or d[i] == "":
                d[i] = "-"
        lead.__dict__ = d
        return lead


    async def chat_inform(self, lead: LeadBase):
        if self.chat_kit == None or self.bot_token == None:
            raise ServiceException("TG TOKENS NOT PROVIDED")

        lead = self.tg_report_filter(lead)

        try:
            request_number = await self.db_service.write_lead(
                lead.lead_name
            )
        except Exception:
            request_number = -1

        if lead.billColor == "red":
            lead.billColor = "красные"
        elif lead.billColor == "blue":
            lead.billColor = "синие"
        elif lead.billColor == "unset":
            lead.billColor = "нет предпочтения"
        message = (
            f"Заявка: `{lead.request_id}` \n"
            f"#Обменов_было : {request_number}\n"
            f"{lead.statuses} \n"
            f"1. Обменник: {lead.site} \n"
            f"2. Лид: {lead.lead_name} \n"
            f"3. Направление обмена: {lead.direction} \n"
            f"4. Место: {lead.place} \n"
            f"5. Комментарий: {lead.description} \n"
            f"6. Объём фиата: {lead.fiat_amount} \n"
            f"7. Объём крипты: {lead.crypto_amount} \n"
            f'8. Время: {datetime.fromtimestamp(int(lead.meet_time)).astimezone(self.tz).strftime("%d-%m-%y %H:%M")} \n'
            f"9. Кошелёк: {lead.wallet} \n"
            f"10. Курс: {lead.exchange_rate} \n"
            f"11. Платформа: {lead.platform} \n"
            f"12. Процент: {lead.percent} \n"
            f"13. Город: {lead.city} \n"
            f"14. Номер карты: {lead.card_number} \n"
            f"15. Купюры: {lead.billColor} \n"
            f"16. Аккаунт: {lead.account} \n"
            f"17. ФИО: {lead.fio} \n"
        )
        if "#Арбитраж" in lead.statuses:
            message += f"17. Айди чата: {lead.chat_id}\n"
        message = message.translate(
            str.maketrans(
                {
                    "-": r"\-",
                    "+": r"\+",
                    "=": r"\=",
                    "|": r"\|",
                    "{": r"\{",
                    "}": r"\}",
                    "#": r"\#",
                    ">": r"\>",
                    "<": r"\<",
                    "]": r"\]",
                    "[": r"\[",
                    "(": r"\(",
                    ")": r"\)",
                    "~": r"\~",
                    "^": r"\^",
                    "$": r"\$",
                    "*": r"\*",
                    ".": r"\.",
                    "!": r"\!",
                    "_": r"\_",
                }
            )
        )

        if lead.city == "Санкт-Петербург":
            chat_id = self.spb_chat_kit
        elif lead.city == "Дубай":
            chat_id = self.dubai_chat_kit
        elif lead.city in {"Стамбул", "Анталья"}:
            chat_id = self.turkey_chat_kit
        else:
            chat_id = self.chat_kit

        await telegram.Bot.send_message(
            chat_id,
            "⚽️ Новый лид! @aviboroda555 @Bakerbtc @yarmoscity @trulyalyash @Batch0707 @arabitonyan @BitMorti",
            timeout=15,
        )
        await telegram.Bot.send_message(
            chat_id,
            message,
            parse_mode=telegram.constants.PARSEMODE_MARKDOWN_V2,
            timeout=15,
        )  # "⚽️ Новый")


