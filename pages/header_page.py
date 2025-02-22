import allure
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):

    @allure.step('Открытие страницы {url}')
    def open_url(self, url):
        self.get_url(url)

    @allure.step('Нажатие на логотип {logo}')
    def click_to_logo(self, logo):
        logo_locator = self.format_locator(HeaderPageLocators.BASE_LOGO_LOCATOR, logo)
        self.click_to_element(logo_locator)

    @allure.step('Переключение на страницу перехода')
    def switch_to_page(self, num):
        self.switch_to_window(num)

    @allure.step('Получение заголовка страницы')
    def get_title_page(self, locator):
        return self.get_text_from_element(locator)