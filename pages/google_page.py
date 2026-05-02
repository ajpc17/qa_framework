from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.google.com")

    def search(self, text):
        box = self.driver.find_element("name", "q")
        box.send_keys(text)
        box.submit()

    def get_title(self):
        return self.driver.title