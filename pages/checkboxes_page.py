from selenium.webdriver.common.by import By

class CheckboxesPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    def marcar_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if not checkboxes[index].is_selected():
            checkboxes[index].click()

    def desmarcar_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if checkboxes[index].is_selected():
            checkboxes[index].click()

    def esta_marcado(self, index):
        return self.get_checkboxes()[index].is_selected()