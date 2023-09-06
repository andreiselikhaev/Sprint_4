from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class InputPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локатор для ввода имени
    name_box = (By.XPATH, "//input[@placeholder='* Имя']")

    # Локатор для ввода фамилии
    surname_box = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Локатор для ввода адреса
    address_box = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Локатор для выбора метро
    metro_box = (By.XPATH, "//input[@placeholder='* Станция метро']")

    # Локатор для ввода номера
    phone_box = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Локатор станции для выбора
    metro_station_box = (By.XPATH, "//button[contains(@class, 'Order_SelectOption__82bhS') and @value='1']")

    # Локатор для кнопки "Далее"
    next_box = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Далее']")


    def input_name(self, name):
        name_box = self.wait.until(EC.element_to_be_clickable(InputPage.name_box))
        name_box.send_keys(name)

    def input_surname(self, surname):
        surname_box = self.wait.until(EC.element_to_be_clickable(InputPage.surname_box))
        surname_box.send_keys(surname)

    def input_address(self, address):
        address_box = self.wait.until(EC.element_to_be_clickable(InputPage.address_box))
        address_box.send_keys(address)

    def input_metro(self):
        metro_box = self.wait.until(EC.element_to_be_clickable(InputPage.metro_box))
        metro_box.click()
        metro_station_box = self.wait.until(EC.element_to_be_clickable(InputPage.metro_station_box))
        metro_station_box.click()


    def input_phone(self, phone):
        phone_box = self.wait.until(EC.element_to_be_clickable(InputPage.phone_box))
        phone_box.send_keys(phone)

    def click_next(self):
        next_box = self.wait.until(EC.element_to_be_clickable(InputPage.next_box))
        self.driver.execute_script("arguments[0].scrollIntoView();", next_box)
        next_box.click()