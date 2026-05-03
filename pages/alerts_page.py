from selenium.webdriver.common.by import By

class AlertsPage:
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_alert(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

    def click_confirm(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    def click_prompt(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

    def aceptar_alerta(self):
        self.driver.switch_to.alert.accept()

    def cancelar_alerta(self):
        self.driver.switch_to.alert.dismiss()

    def escribir_en_alerta(self, texto):
        alerta = self.driver.switch_to.alert
        alerta.send_keys(texto)
        alerta.accept()

    def get_resultado(self):
        return self.driver.find_element(By.ID, "result").text