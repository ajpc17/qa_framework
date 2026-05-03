from pages.login_page import LoginPage

def test_login_exitoso(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.get_success_message()

def test_login_password_incorrecta(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "password_incorrecta")
    assert "Your password is invalid!" in page.get_error_message()

def test_login_usuario_incorrecto(driver):
    page = LoginPage(driver)
    page.open()
    page.login("usuario_falso", "SuperSecretPassword!")
    assert "Your username is invalid!" in page.get_error_message()