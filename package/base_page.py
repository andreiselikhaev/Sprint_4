from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def scroll_until_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_button(self, locator):
        element_box = self.wait.until(EC.element_to_be_clickable(locator))
        element_box.click()

    def input_text(self, locator, text):
        element_box = self.wait.until(EC.element_to_be_clickable(locator))
        element_box.send_keys(text)
        element_box.send_keys(Keys.ENTER)

    def wait_element_located(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def wait_element_clickable(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        return button

    def wait_window_is_opened(self):
        self.wait.until(EC.new_window_is_opened)




