import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
YANDEXGPT_API_KEY = os.getenv("YANDEXGPT_API_KEY")
YANDEX_FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")

# URLs программ
PROGRAM_AI_URL = "https://abit.itmo.ru/program/master/ai"
PROGRAM_AI_PRODUCT_URL = "https://abit.itmo.ru/program/master/ai_product"

# Путь к данным
DATA_DIR = "data/processed"
os.makedirs(DATA_DIR, exist_ok=True)