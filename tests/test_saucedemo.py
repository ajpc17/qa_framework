from pages.saucedemo_login_page import SaucedemoLoginPage
from pages.saucedemo_productos_page import SaucedemoProductosPage

def test_login_exitoso(driver):
    page = SaucedemoLoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert page.get_titulo_pagina() == "Products"

def test_login_usuario_bloqueado(driver):
    page = SaucedemoLoginPage(driver)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "locked out" in page.get_error_message()

def test_login_password_incorrecta(driver):
    page = SaucedemoLoginPage(driver)
    page.open()
    page.login("standard_user", "password_incorrecta")
    assert "do not match" in page.get_error_message()

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