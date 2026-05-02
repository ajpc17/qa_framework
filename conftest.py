import pytest
import os
from utils.driver import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports", exist_ok=True)
            driver.save_screenshot(
                f"reports/{item.name}.png"
            )