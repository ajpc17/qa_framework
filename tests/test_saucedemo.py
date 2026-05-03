import pytest
from pages.saucedemo_login_page import SaucedemoLoginPage
from pages.saucedemo_productos_page import SaucedemoProductosPage

# --- Tests normales ---

def test_productos_visibles(driver):
    login = SaucedemoLoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    productos = SaucedemoProductosPage(driver)
    assert len(productos.get_productos()) == 6

def test_agregar_al_carrito(driver):
    login = SaucedemoLoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    productos = SaucedemoProductosPage(driver)
    productos.agregar_primer_producto()
    assert productos.get_cantidad_carrito() == "1"

# --- Data Driven Testing ---

@pytest.mark.parametrize("usuario,password,esperado", [
    ("standard_user",   "secret_sauce",      "Products"),
    ("locked_out_user", "secret_sauce",      "locked out"),
    ("invalid_user",    "wrong_pass",        "do not match"),
    ("standard_user",   "wrong_pass",        "do not match"),
    ("",                "",                  "Username is required"),
])
def test_login_data_driven(driver, usuario, password, esperado):
    page = SaucedemoLoginPage(driver)
    page.open()
    page.login(usuario, password)
    assert esperado in driver.page_source