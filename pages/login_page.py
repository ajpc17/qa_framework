from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import WAIT_TIME

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def get_success_message(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        return element.text

    def get_error_message(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        )
        return element.text