from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.config import BASE_URL, WAIT_TIME

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def open(self):
        self.driver.get(BASE_URL)

    def search(self, text):
        box = self.driver.find_element("name", "q")
        box.send_keys(text)
        box.submit()

    def get_title(self):
        return self.driver.title