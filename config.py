from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

ADMIN_ID = os.getenv("ADMIN_ID")