from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import WAIT_TIME

class SaucedemoProductosPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def get_productos(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item")

    def agregar_primer_producto(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn_primary").click()

    def get_cantidad_carrito(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text

    def ir_al_carrito(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()