import config
from PageObject import ScooterMain
import pytest
import allure

class TestScooterMain:
    # Проверка кнопки Заказать из шапки
    @allure.title('Проверка кнопки Заказать из шапки')
    def test_check_header_order_button(self, driver, main_page):
        expected_url = config.order_url
        main_page.click_header_order_button()
        assert expected_url == driver.current_url

    # Проверка кнопки Заказать из середины страницы
    @allure.title('Проверка кнопки Заказать из середины страницы')
    def test_check_main_order_button(self, driver, main_page):
        expected_url = config.order_url
        main_page.accept_cookies_button()
        main_page.scroll_to_order_button_main()
        main_page.click_order_button_main()
        assert expected_url == driver.current_url

    # Проверка раздела FAQ. Выполняется за одну сессию
    @allure.title('Проверка Полей ответы на вопросы')
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (ScooterMain.question1, ScooterMain.answer1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (ScooterMain.question2, ScooterMain.answer2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (ScooterMain.question3, ScooterMain.answer3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (ScooterMain.question4, ScooterMain.answer4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (ScooterMain.question5, ScooterMain.answer5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (ScooterMain.question6, ScooterMain.answer6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (ScooterMain.question7, ScooterMain.answer7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (ScooterMain.question8, ScooterMain.answer8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    def test_check_faq_accordion(self, main_page, question_locator, answer_locator, expected_answer):
        main_page.scroll_to_faq()
        main_page.click_faq_question(question_locator)
        main_page.check_faq_answer(answer_locator, expected_answer)
