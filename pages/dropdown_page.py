from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def seleccionar_opcion(self, valor):
        dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_value(valor)

    def get_opcion_seleccionada(self):
        dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
        return dropdown.first_selected_option.text