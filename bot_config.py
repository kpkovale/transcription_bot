import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import URL
import logging


LOG_LEVEL = logging.INFO

# initiate StateStorage and bot
BASE_DIR = Path(__file__).parent.resolve()
load_dotenv(os.path.join(BASE_DIR, '.env'))
TOKEN = os.getenv("TOKEN")
KEYS_FILE = os.path.join(BASE_DIR, "authorized_key.json")

# load database connection string params from .env
DB_STRING = 'sqlite:///my_db.db'
# DB_STRING = URL.create(
#     "postgresql+psycopg2",
#     username=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),  # plain (unescaped) text
#     host=os.getenv("DB_HOST"),
#     port=os.getenv("DB_PORT"),
#     database=os.getenv("DB_NAME"),
# )

# specify provider_token in .env file if payments connected
#PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN") # @BotFather -> Bot Settings -> Payments
