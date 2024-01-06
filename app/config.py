import os
from pytz import timezone

from dotenv import load_dotenv

load_dotenv()

# DB SETTINGS

POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

POSTGRES_DSN = f"user={POSTGRES_USER} password={POSTGRES_PASSWORD} host={POSTGRES_HOST} port={POSTGRES_PORT} dbname={POSTGRES_DB}"

#TOWER SERVICE SETTINGS
TOWER_PASS_CREATOR_URL = os.environ.get("TOWER_PASS_CREATOR_URL")
TOWER_PASS_CREATOR_TOKEN = os.environ.get("TOWER_PASS_CREATOR_TOKEN")

# CRM SERVICE SETTINGS
CRM_API_URL = os.environ.get("CRM_API_URL")
CRM_WEBHOOK_KEY = os.environ.get("CRM_WEBHOOK_KEY")

# TG SERVICE SETTINGS

TIMEZONE = timezone("Europe/Moscow") 
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
TG_TOKEN = os.environ.get("TG_CHAT_TOKEN"),
CHAT_KIT = int(os.environ.get("WHALE_TG_CHAT", "0")),
SPB_CHAT_KIT = int(os.environ.get("SPB_WHALE_CHAT_ID", "0")),
DUBAI_CHAT_KIT = int(os.environ.get("DUBAI_WHALE_CHAT_ID", "0")),
TURKEY_CHAT_KIT = int(os.environ.get("TURKEY_WHALE_CHAT_ID", "0")),


# LEAD SERVICE SETTINGS

ACCOUNTS = [
    "Ксюша",
    "Птичка",
    "Вика кит",
    "Люда кит",
    "Артур Кит",
    "Люба Кит",
    "Аккаунт cryptohub",
    "Ксюша Реф",
    "Макс Кит",
    "Франческо",
    "Айка кит",
    "Полина кит",
    "Восторг кит",
    "Бону кит",
    ]

LEAD_TYPE = "Usual"
STATUS_BUY= ["#офис", "#другие_города", "#Арбитраж"]

STATUS_SELL = [
    "#Покупка",
    "#Продажа",
    "#Новый",
    "#Постоянник",
    "#Икринка",
    "#Кит",
    "#КлючевойКит",
    "#Арбитраж",
    "#NPS",
    "#СтарыйКлиент",
]

CITIES = [
    "Москва",
    "Санкт-Петербург",
    "Амстердам",
    "Анапа",
    "Анталья",
    "Архангельск",
    "Астрахань",
    "Барселона",
    "Брянск",
    "Белгород",
    "Берлин",
    "Валенсия",
    "Варшава",
    "Владивосток",
    "Владикавказ",
    "Вильнюс",
    "Волгоград",
    "Воронеж",
    "Геленджик",
    "Грозный",
    "Дубай",
    "Дублин",
    "Екатеринбург",
    "Ижевск",
    "Иркутск",
    "Йошкар-Ола",
    "Казань",
    "Калининград",
    "Калуга",
    "Кемерово",
    "Киров",
    "Киев",
    "Кострома",
    "Краснодар",
    "Красноярск",
    "Курск",
    "Липецк",
    "Лондон",
    "Магнитогорск",
    "Махачкала",
    "Майами",
    "Мадрид",
    "Малага",
    "Милан",
    "Минск",
    "Мурманск",
    "Набережные Челны",
    "Нижний Новгород",
    "Новокузнецк",
    "Новороссийск",
    "Новосибирск",
    "Омск",
    "Орел",
    "Оренбург",
    "Париж",
    "Пенза",
    "Пермь",
    "Прага",
    "Пятигорск",
    "Рига",
    "Ростов-на-Дону",
    "Рязань",
    "Самара",
    "Саранск",
    "Саратов",
    "Симферополь",
    "Сочи",
    "Ставрополь",
    "Стамбул",
    "Старый Оскол",
    "Таганрог",
    "Тамбов",
    "Тверь",
    "Тула",
    "Тюмень",
    "Уфа",
    "Чебоксары",
    "Челябинск",
    "Череповец",
    "Ярославль",
    "Стамбул",
    "Ереван",
    "Анталья",
    "Тбилиси",
    "Бишкек",
    "Алма-Ата",
    "Пхукет",
]

PLACES = ["офис", "внизу", "доставка по городу", "залив на карту"]

FIAT_CURRENCIES = [
    "RUB",
    "USD",
    "EUR",
    "TRY",
    "AED",
    "AMD",
    "KZT",
    "GEL",
    "SOM",
    "THB"
]

CRYPTO_CURRUNCIES = [
    "BTC",
    "ETH",
    "ALT",
    "USDT",
    "USDC",
    "BUSD",
    "DAI",
    "TUSD",
    "USDP",
]
