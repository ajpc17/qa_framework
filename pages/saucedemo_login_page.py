from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import WAIT_TIME

class SaucedemoLoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container"))
        ).text

    def get_titulo_pagina(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
        ).text