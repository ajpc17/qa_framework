from pages.alerts_page import AlertsPage

def test_alert_simple(driver):
    page = AlertsPage(driver)
    page.open()
    page.click_alert()
    page.aceptar_alerta()
    assert page.get_resultado() == "You successfully clicked an alert"

def test_confirm_aceptar(driver):
    page = AlertsPage(driver)
    page.open()
    page.click_confirm()
    page.aceptar_alerta()
    assert page.get_resultado() == "You clicked: Ok"

def test_confirm_cancelar(driver):
    page = AlertsPage(driver)
    page.open()
    page.click_confirm()
    page.cancelar_alerta()
    assert page.get_resultado() == "You clicked: Cancel"

def test_prompt_con_texto(driver):
    page = AlertsPage(driver)
    page.open()
    page.click_prompt()
    page.escribir_en_alerta("Hola QA")
    assert page.get_resultado() == "You entered: Hola QA"