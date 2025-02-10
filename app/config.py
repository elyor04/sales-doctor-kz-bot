import os
import time
from dotenv import load_dotenv

load_dotenv()
time.tzset()

CRM_BASE_URL = os.getenv("CRM_BASE_URL").rstrip("/") + "/"
CRM_TOKEN = os.getenv("CRM_TOKEN")
BOT_TOKEN = os.getenv("BOT_TOKEN")

DOMAIN_NAME = os.getenv("DOMAIN_NAME").rstrip("/") + "/"
CRM_WEBHOOK = os.getenv("CRM_WEBHOOK")
BOT_WEBHOOK = os.getenv("BOT_WEBHOOK")

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
CHAT_ID = int(os.getenv("CHAT_ID"))
