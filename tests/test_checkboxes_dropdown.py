from pages.checkboxes_page import CheckboxesPage
from pages.dropdown_page import DropdownPage

def test_marcar_checkbox(driver):
    page = CheckboxesPage(driver)
    page.open()
    page.marcar_checkbox(0)
    assert page.esta_marcado(0) == True

def test_desmarcar_checkbox(driver):
    page = CheckboxesPage(driver)
    page.open()
    page.desmarcar_checkbox(1)
    assert page.esta_marcado(1) == False

def test_dropdown_opcion_1(driver):
    page = DropdownPage(driver)
    page.open()
    page.seleccionar_opcion("1")
    assert page.get_opcion_seleccionada() == "Option 1"

def test_dropdown_opcion_2(driver):
    page = DropdownPage(driver)
    page.open()
    page.seleccionar_opcion("2")
    assert page.get_opcion_seleccionada() == "Option 2"