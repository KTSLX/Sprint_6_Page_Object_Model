import config
import locators
import pytest
import data
from PageObject import ScooterOrder
from selenium.webdriver.common.by import By
import allure

class TestOrder:
    # Проверка лого - переход на Яндекс
    @allure.title('Проверка лого - переход на Яндекс')
    def test_check_header_logo_yandex_new_window(self, driver):
        driver.get(config.order_url)
        test_order = ScooterOrder(driver)
        test_order.accept_cookies_button()
        test_order.click_header_logo_yandex()
        test_order.wait_for_new_window_and_switch()
        test_order.verify_url()

    # Проверка лого - переход на главную
    @allure.title('Проверка лого - переход на главную')
    def test_check_header_logo_scooter(self, driver):
        expected_url = 'https://qa-scooter.praktikum-services.ru/'
        driver.get(config.order_url)
        test_order = ScooterOrder(driver)
        test_order.click_header_logo_scooter()
        assert driver.current_url == expected_url

    # Проверка оформления заказа с двумя наборами данных
    # Данные можно дополнить в data.py
    @allure.title('Проверка создания заказа с корректными данным')
    @pytest.mark.parametrize("order_data", [
        {field: value for field, value in zip(data.test_data.keys(), values)}
        for values in zip(*data.test_data.values())
    ], indirect=True)
    def test_order_successfull(self, driver, order_data):
        driver.get(config.order_url)
        test_order = ScooterOrder(driver)
#       test_order.accept_cookies_button()
        # filling in the form
        test_order.set_name(order_data["name"])
        test_order.set_surname(order_data["surname"])
        test_order.set_address(order_data["address"])
        test_order.set_metro_station(order_data["station"])
        test_order.set_telephone_number(order_data["phone"])
        test_order.click_button_next()
        test_order.set_date(order_data["date"])
        test_order.set_term(order_data["term"])
        test_order.select_scooter_color(order_data["color"])
        test_order.set_comment(order_data["comment"])
        test_order.click_order_button()
        test_order.click_order_confirmation_button()
        order_successful = driver.find_element(By.XPATH, locators.header_completed_order_confirmation).text
        assert "Заказ оформлен" in order_successful

