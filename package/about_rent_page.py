from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class InputRentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локатор для ввода даты
    calendar_box = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # Локатор для выбора срока аренды
    rental_period_box = (By.XPATH, "//div[@class='Dropdown-placeholder']")

    # Локатор кнопки "сутки"
    one_day_box = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")

    # Локатор выбора цвета самоката
    color_black_box = (By.XPATH, "//input[@id='black']")

    # Локатор для ввода комментария
    comment_box = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Локатор для поиска блока нижних кнопок
    buttons_block = (By.CLASS_NAME, "Order_Buttons__1xGrp")

    # Локатор кнопки "Заказать"
    order_box = (By.XPATH, 'button[text()="Заказать"]')

    # Локатор кнопки "Да" при подтверждении заказа
    confirm_box = (By.XPATH, 'button[text()="Да"]')

    # Локатор блока с текстом "Заказ оформлен"
    successful_order = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")


    def choose_day(self, date):
        calendar_box = self.wait.until(EC.element_to_be_clickable(InputRentPage.calendar_box))
        calendar_box.send_keys(date)
        calendar_box.send_keys(Keys.ENTER)

    def choose_rental_period(self):
        rental_period_box = self.wait.until(EC.element_to_be_clickable(InputRentPage.rental_period_box))
        rental_period_box.click()

        one_day_box = self.wait.until(EC.element_to_be_clickable(InputRentPage.one_day_box))
        one_day_box.click()

    def choose_color(self):
        color_black_box = self.wait.until(EC.element_to_be_clickable(InputRentPage.color_black_box))
        color_black_box.click()

    def insert_comment(self, comment):
        comment_box = self.wait.until(EC.element_to_be_clickable(InputRentPage.comment_box))
        comment_box.send_keys(comment)
        comment_box.send_keys(Keys.ENTER)

    def click_order(self):
        buttons_block = self.wait.until(EC.presence_of_element_located(InputRentPage.buttons_block))

        order_box = buttons_block.find_element(*InputRentPage.order_box)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_box)
        order_box.click()

        buttons_block = self.wait.until(EC.presence_of_all_elements_located(InputRentPage.buttons_block))
        confirm_block = buttons_block[1]
        confirm_box = confirm_block.find_element(*InputRentPage.confirm_box)
        confirm_box.click()

        successful_order_text = self.driver.find_element(*InputRentPage.successful_order).text
        return successful_order_text









