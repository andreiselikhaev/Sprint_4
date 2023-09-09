from package.main_page import MainPage
import allure

@allure.feature("Проверка перенаправления")
class TestRedirect():
    @allure.title("Проверка перенаправления на главную страницу")
    def test_scooter_button(self, browser):
        with allure.step("Открываем главную страницу"):
            browser.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(browser)
        with allure.step("Нажимаем на заказ"):
            main_page.make_an_order_click("first")
        with allure.step("Нажимаем на Самокат"):
            main_page.click_scooter_logo()
        with allure.step("Получаем текст с главной страницы"):
            main_page_text = main_page.find_main_page_text()
        assert "Самокат" in main_page_text, 'Не удалось перейти на главную страницу'

    @allure.title("Проверка перенаправления на страницу Яндекса")
    def test_yandex_button(self, browser):
        with allure.step("Открываем главную страницу"):
            browser.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(browser)
        with allure.step("Открываем страницу яндекса и получаем блок для поиска"):
            main_page.click_yandex_logo()
            new_tab_url = main_page.check_new_tab()

        expected_url = "https://dzen.ru/?yredirect=true"
        assert new_tab_url == expected_url, 'Не удалось перейти на страницу Яндекса'
