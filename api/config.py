from dotenv import load_dotenv
import os

load_dotenv()

PASS = os.getenv('DB_PASSWORD')
USER = os.getenv('DB_USER')
DB = os.getenv('DB')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

