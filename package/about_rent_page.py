from selenium.webdriver.common.by import By
from package.base_page import BasePage

class InputRentPage(BasePage):
    calendar_box = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period_box = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    one_day_box = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    color_black_box = (By.XPATH, "//input[@id='black']")
    comment_box = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    buttons_block = (By.CLASS_NAME, "Order_Buttons__1xGrp")
    order_box = (By.XPATH, 'button[text()="Заказать"]')
    confirm_box = (By.XPATH, '//button[text()="Да"]')
    successful_order = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")

    def choose_day(self, date):
        BasePage.input_text(self, InputRentPage.calendar_box, date)

    def choose_rental_period(self):
        self.click_button(InputRentPage.rental_period_box)
        self.click_button(InputRentPage.one_day_box)

    def choose_color(self):
        self.click_button(InputRentPage.color_black_box)

    def insert_comment(self, comment):
        BasePage.input_text(self, InputRentPage.comment_box, comment)

    def get_order_text(self):
        buttons_block = BasePage.wait_element_clickable(self, InputRentPage.buttons_block)
        order_box = buttons_block.find_element(*InputRentPage.order_box)
        order_box.click()

        self.click_button(InputRentPage.confirm_box)

        successful_order_text = self.driver.find_element(*InputRentPage.successful_order).text
        return successful_order_text
