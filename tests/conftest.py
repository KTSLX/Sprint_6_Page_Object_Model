import pytest
from selenium import webdriver
from config import BASE_URL
from PageObject import ScooterMain


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    driver.get(BASE_URL)
    main_page = ScooterMain(driver)
    yield main_page


@pytest.fixture(scope="function")
def order_data(request):
    return request.param
