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
        self._cerrar_anuncio()

    def _cerrar_anuncio(self):
        try:
            boton = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "div[id='ad_position_box'] button")
                )
            )
            boton.click()
        except:
            pass

    def login(self, email, password):
        self.wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "[data-qa='login-button']"
        ).click()

    def login_exitoso(self):
        return "Logged in as" in self.driver.page_source