from package.main_page import MainPage
from package.user_info_page import InputPage
from package.about_rent_page import InputRentPage
import time
import pytest
import allure

@allure.feature("Заказ самоката")
class TestOrder:
    @pytest.mark.parametrize("type_order_box, name, surname, address, phone, comment, date, expected_message", [
        ("first", "Вася", "Пупкин", "ул.Лихачева", "88005553535", 'Тест на selenium', "06.09.2023", "Заказ оформлен"),
        ("second", "Андрей", "Миронов", "ул.Лихачева", "88005553535", 'Тест на selenium', "06.09.2023", "Заказ оформлен"),
        # Добавьте другие наборы параметров и ожидаемых результатов по вашему усмотрению
    ])
    def test_order(self, browser, type_order_box, name, surname, address, phone, comment, date, expected_message):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.confirm_cookie()
        main_page.make_an_order_click(type_order_box)

        input_page = InputPage(browser)
        input_page.input_name(name)
        input_page.input_surname(surname)
        input_page.input_address(address)
        input_page.input_metro()
        input_page.input_phone(phone)
        input_page.click_next()

        input_rent_page = InputRentPage(browser)
        input_rent_page.choose_day(date)
        input_rent_page.choose_rental_period()
        input_rent_page.choose_color()
        input_rent_page.insert_comment(comment)
        successful_order_text = input_rent_page.click_order()

        assert expected_message in successful_order_text, "Не удалось совершить заказ"





