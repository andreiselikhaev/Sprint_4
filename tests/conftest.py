import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
