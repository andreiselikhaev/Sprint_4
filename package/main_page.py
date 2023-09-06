from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локатор для скролла до вопросов
    text_element = (By.XPATH, "//div[contains(@class, 'Home_SubHeader__zwi_E') and text()='Вопросы о важном']")

    # Локатор кнопки заказа
    order_box = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')]")

    # Локатор для кнопки "Самокат"
    scooter_box = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")

    # Локатор текст на главное странице
    main_page_text = (By.CSS_SELECTOR, '.Home_Header__iJKdX')

    # Локатор для кнопки "Яндекс"
    yandex_box = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    # Локатор для кнопки куки
    confirm_cookie_box = (By.XPATH, "//button[@class='App_CookieButton__3cvqF']")

    def confirm_cookie(self):
        button = self.wait.until(EC.element_to_be_clickable(MainPage.confirm_cookie_box))
        button.click()

    def find_question(self, question_number):
        text_element = self.wait.until(EC.presence_of_element_located(MainPage.text_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", text_element)

        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@id="accordion__heading-{question_number}"]')))
        button.click()

    def find_answer(self, question_number):
        answer_text = self.driver.find_element(By.XPATH, f'//div[@id="accordion__panel-{question_number}"]')
        actual_text = answer_text.find_element(By.TAG_NAME, 'p').text
        return actual_text

    def make_an_order_click(self, type_order_box):
        order_boxs = self.driver.find_elements(*MainPage.order_box)
        if type_order_box == 'first':
            order_boxs[0].click()
        elif type_order_box == 'second':
            order_boxs[1].click()

    def find_scooter_logo(self):
        scooter_box = self.wait.until(EC.element_to_be_clickable(MainPage.scooter_box))
        scooter_box.click()

    def find_main_page_text(self):
        main_page_text = self.wait.until(EC.presence_of_element_located(MainPage.main_page_text))
        return main_page_text.text

    def find_yandex_logo(self):
        yandex_box = self.wait.until(EC.element_to_be_clickable(MainPage.yandex_box))
        yandex_box.click()
        self.wait.until(EC.new_window_is_opened)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def check_new_tab(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dzen-search-arrow-common')))
        new_tab_url = self.driver.current_url
        return new_tab_url



