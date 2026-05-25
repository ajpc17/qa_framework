# NOTA: estos tests fallan porque automationexercise.com
# tiene proteccion anti-bot (Cloudflare) que bloquea Selenium.
# El codigo es correcto - el sitio detecta automatizacion.


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import WAIT_TIME

class AutoexerciseRegisterPage:
    URL = "https://automationexercise.com/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def open(self):
        self.driver.get(self.URL)

    def registrar(self, nombre, email):
        self.driver.find_element(
            By.CSS_SELECTOR, "[data-qa='signup-name']"
        ).send_keys(nombre)
        self.driver.find_element(
            By.CSS_SELECTOR, "[data-qa='signup-email']"
        ).send_keys(email)
        self.driver.find_element(
            By.CSS_SELECTOR, "[data-qa='signup-button']"
        ).click()

    def email_ya_existe(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".signup-form p"))
        ).text

    def redirige_a_registro(self):
        return "signup" in self.driver.current_url