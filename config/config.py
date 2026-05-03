import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.saucedemo.com"
BROWSER = "chrome"
WAIT_TIME = 10

SAUCE_USER = os.getenv("SAUCE_USER")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")