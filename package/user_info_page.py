from selenium.webdriver.common.by import By
from package.base_page import BasePage

class InputPage(BasePage):
    name_box = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_box = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_box = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_box = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_box = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    metro_station_box = (By.XPATH, "//button[contains(@class, 'Order_SelectOption__82bhS') and @value='1']")
    next_box = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Далее']")

    def input_name(self, name):
        self.input_text(InputPage.name_box, name)

    def input_surname(self, surname):
        self.input_text(InputPage.surname_box, surname)

    def input_address(self, address):
        self.input_text(InputPage.address_box, address)

    def input_metro(self):
        self.click_button(InputPage.metro_box)
        self.click_button(InputPage.metro_station_box)

    def input_phone(self, phone):
        self.input_text(InputPage.phone_box, phone)

    def click_next(self):
        next_box = BasePage.wait_element_clickable(self, InputPage.next_box)
        self.scroll_until_element(next_box)
        next_box.click()
