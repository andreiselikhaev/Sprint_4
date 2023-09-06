import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()

    wait = WebDriverWait(driver, 10)  # Максимальное время ожидания
    driver.wait = wait

    yield driver
    driver.quit()