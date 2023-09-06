from package.main_page import MainPage
import allure

@allure.feature("Проверка перенаправления")
class TestRedirect():
    def test_scooter_button(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.make_an_order_click("first")
        main_page.find_scooter_logo()
        main_page_text = main_page.find_main_page_text()
        assert "Самокат" in main_page_text

    def test_yandex_button(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.make_an_order_click("first")
        main_page.find_yandex_logo()
        new_tab_url = main_page.check_new_tab()

        # Проверяем URL на соответствие ожидаемому
        expected_url = "https://dzen.ru/?yredirect=true"  # Замените на ожидаемый URL
        assert new_tab_url == expected_url, f"URL не соответствует ожидаемому. Ожидался {expected_url}, получено {new_tab_url}"
