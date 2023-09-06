from package.main_page import MainPage
import allure

@allure.feature("Проверка вопросов")
class TestsQuestions:
    def test_first_question(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.find_question(0)
        answer = main_page.find_answer(0)
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in answer, "Первый вопрос не удалось проверить"

    def test_second_question(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.find_question(1)
        answer = main_page.find_answer(1)
        assert "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим." in answer, "Второй вопрос не удалось проверить"

    def test_third_question(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.find_question(2)
        answer = main_page.find_answer(2)
        assert "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30." in answer, "Третий вопрос не удалось проверить"

    def test_fourth_question(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.find_question(3)
        answer = main_page.find_answer(3)
        assert "Только начиная с завтрашнего дня. Но скоро станем расторопнее." in answer, "Четвертый вопрос не удалось проверить"

    def test_fifth_question(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.find_question(4)
        answer = main_page.find_answer(4)
        assert "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010." in answer, "Пятый вопрос не удалось проверить"

    def test_sixth_question(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.find_question(5)
        answer = main_page.find_answer(5)
        assert "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится." in answer, "Шестой вопрос не удалось проверить"

    def test_seventh_question(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.find_question(6)
        answer = main_page.find_answer(6)
        assert "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои." in answer, "Седьмой вопрос не удалось проверить"

    def test_eighth_question(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(browser)
        main_page.find_question(7)
        answer = main_page.find_answer(7)
        assert "Да, обязательно. Всем самокатов! И Москве, и Московской области." in answer, "Седьмой вопрос не удалось проверить"




