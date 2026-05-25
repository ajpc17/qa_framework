
import pytest
import time
from pages.autoexercise_register_page import AutoexerciseRegisterPage

def test_registro_email_existente(driver):
    page = AutoexerciseRegisterPage(driver)
    page.open()
    page.registrar("TestQA", "testqa.farma@gmail.com")
    assert "Email Address already exist!" in page.email_ya_existe()

def test_registro_nuevo_usuario_redirige(driver):
    page = AutoexerciseRegisterPage(driver)
    page.open()
    page.registrar("TestQA", f"testqa{int(time.time())}@gmail.com")
    assert page.redirige_a_registro()

@pytest.mark.parametrize("nombre,email,esperado", [
    ("TestQA", "testqa.farma@gmail.com", "already exist"),
    ("Nuevo User",  f"nuevo{int(time.time())}@gmail.com", "signup"),
   
])
def test_registro_data_driven(driver, nombre, email, esperado):
    page = AutoexerciseRegisterPage(driver)
    page.open()
    page.registrar(nombre, email)
    assert esperado in driver.page_source