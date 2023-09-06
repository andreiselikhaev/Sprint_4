from selenium.webdriver.common.by import By
from package.base_page import BasePage

class MainPage(BasePage):
    text_element = (By.XPATH, "//div[contains(@class, 'Home_SubHeader__zwi_E') and text()='Вопросы о важном']")
    order_box = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')]")
    scooter_box = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    main_page_text = (By.CSS_SELECTOR, '.Home_Header__iJKdX')
    yandex_box = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    confirm_cookie_box = (By.XPATH, "//button[@class='App_CookieButton__3cvqF']")
    actual_text = (By.TAG_NAME, 'p')
    yandex_search = (By.CLASS_NAME, 'dzen-search-arrow-common')
    question_buttons = [(By.XPATH, '//div[@id="accordion__heading-0"]'),
                        (By.XPATH, '//div[@id="accordion__heading-1"]'),
                        (By.XPATH, '//div[@id="accordion__heading-2"]'),
                        (By.XPATH, '//div[@id="accordion__heading-3"]'),
                        (By.XPATH, '//div[@id="accordion__heading-4"]'),
                        (By.XPATH, '//div[@id="accordion__heading-5"]'),
                        (By.XPATH, '//div[@id="accordion__heading-6"]'),
                        (By.XPATH, '//div[@id="accordion__heading-7"]')]
    question_answers = [(By.XPATH, '//div[@id="accordion__panel-0"]'),
                        (By.XPATH, '//div[@id="accordion__panel-1"]'),
                        (By.XPATH, '//div[@id="accordion__panel-2"]'),
                        (By.XPATH, '//div[@id="accordion__panel-3"]'),
                        (By.XPATH, '//div[@id="accordion__panel-4"]'),
                        (By.XPATH, '//div[@id="accordion__panel-5"]'),
                        (By.XPATH, '//div[@id="accordion__panel-6"]'),
                        (By.XPATH, '//div[@id="accordion__panel-7"]'),
                        ]

    def confirm_cookie(self):
        BasePage.click_button(self, MainPage.confirm_cookie_box)

    def find_question(self, question_number):
        text_element = self.wait_element_located(MainPage.text_element)
        self.scroll_until_element(text_element)
        MainPage.click_button(self, MainPage.question_buttons[question_number])

    def find_answer(self, question_number):
        answer_text = self.driver.find_element(*MainPage.question_answers[question_number])
        actual_text = answer_text.find_element(*MainPage.actual_text).text
        return actual_text

    def make_an_order_click(self, type_order_box):
        order_boxs = self.driver.find_elements(*MainPage.order_box)
        if type_order_box == 'first':
            order_boxs[0].click()
        elif type_order_box == 'second':
            order_boxs[1].click()

    def click_scooter_logo(self):
        scooter_box = self.wait_element_clickable(MainPage.scooter_box)
        scooter_box.click()

    def find_main_page_text(self):
        main_page_text = self.wait_element_located(MainPage.main_page_text)
        return main_page_text.text

    def click_yandex_logo(self):
        yandex_box = self.wait_element_clickable(MainPage.yandex_box)
        yandex_box.click()
        self.wait_window_is_opened()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def check_new_tab(self):
        self.wait_element_located(MainPage.yandex_search)
        new_tab_url = self.driver.current_url
        return new_tab_url
