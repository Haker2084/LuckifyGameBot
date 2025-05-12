import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TONKEEPER_WALLET = os.getenv("TONKEEPER_WALLET")