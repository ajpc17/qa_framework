from pages.google_page import GooglePage

def test_titulo_google(driver):
    page = GooglePage(driver)
    page.open()
    assert "Google" in page.get_title()

def test_busqueda(driver):
    page = GooglePage(driver)
    page.open()
    page.search("QA automation")
    assert len(page.get_title()) > 0

    