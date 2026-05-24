from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import WAIT_TIME

class AutomationLoginPage:
    URL = "https://automationexercise.com/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "[data-qa='login-button']"
        ).click()

    def login_exitoso(self):
        return "Logged in as" in self.driver.page_source

    def get_error_message(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form p"))
        ).text