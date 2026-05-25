import pytest
from pages.autoexercise_login_page import AutomationLoginPage

def test_login_credenciales_invalidas(driver):
    page = AutomationLoginPage(driver)
    page.open()
    page.login("invalido@test.com", "wrongpass")
    assert "Your email or password is incorrect" in driver.page_source

@pytest.mark.parametrize("email,password,esperado", [
    ("invalido@test.com",  "wrongpass",  "Your email or password is incorrect"),
    ("invalido2@test.com", "wrongpass2", "Your email or password is incorrect"),
])
def test_login_data_driven(driver, email, password, esperado):
    page = AutomationLoginPage(driver)
    page.open()
    page.login(email, password)
    assert esperado in driver.page_source