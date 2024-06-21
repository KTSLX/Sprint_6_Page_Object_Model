from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import allure

class ScooterMain:

    header_order_button = [By.XPATH, locators.header_order_button]
    header_logo_yandex = [By.XPATH, locators.header_logo_yandex]
    header_logo_scooter = [By.XPATH, locators.header_logo_scooter]
    order_button_main = [By.XPATH, locators.order_button_main]
    accept_cookies_yes = [By.XPATH, locators.accept_cookies_button]

    # Вопросы о важном
    header_faq = [By.XPATH, locators.header_faq]
    # Сколько это стоит и как оплатить?
    question1 = [By.XPATH, locators.question1]
    answer1 = [By.XPATH, locators.answer1]
    question2 = [By.XPATH, locators.question2]
    answer2 = [By.XPATH, locators.answer2]
    question3 = [By.XPATH, locators.question3]
    answer3 = [By.XPATH, locators.answer3]
    question4 = [By.XPATH, locators.question4]
    answer4 = [By.XPATH, locators.answer4]
    question5 = [By.XPATH, locators.question5]
    answer5 = [By.XPATH, locators.answer5]
    question6 = [By.XPATH, locators.question6]
    answer6 = [By.XPATH, locators.answer6]
    question7 = [By.XPATH, locators.question7]
    answer7 = [By.XPATH, locators.answer7]
    question8 = [By.XPATH, locators.question8]
    answer8 = [By.XPATH, locators.answer8]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_load_scooter(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.header_order_button))

    @allure.step('Нажатие принять куки')
    def accept_cookies_button(self):
        self.driver.find_element(*self.accept_cookies_yes).click()

    @allure.step('Нажатие кнопки Заказать из хедера страницы')
    def click_header_order_button(self):
        self.driver.find_element(*self.header_order_button).click()

    @allure.step('Скролл до кнопки Заказать в середине страницы')
    def scroll_to_order_button_main(self):
        element = self.driver.find_element(*self.order_button_main)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_button_main))

    @allure.step('Нажатие на кнопку Заказать в середине страницы')
    def click_order_button_main(self):
        self.driver.find_element(*self.order_button_main).click()

    @allure.step('Прокрутка до раздела FAQ')
    def scroll_to_faq(self):
        element = self.driver.find_element(*self.header_faq)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.header_faq))

    @allure.step('Нажатие на вопрос в разделе FAQ')
    def click_faq_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    @allure.step('Проверка ответа в разделе FAQ')
    def check_faq_answer(self, answer_locator, expected_answer):
        answer = self.driver.find_element(*answer_locator).text
        assert answer == expected_answer, f"Expected answer: {expected_answer}, but got: {answer}"
class ScooterOrder:

    accept_cookies_yes = [By.XPATH, locators.accept_cookies_button]
    input_name = [By.XPATH, locators.input_name_field]
    input_surname = [By.XPATH, locators.input_surname_field]
    input_address = [By.XPATH, locators.input_address_field]
    metro_list = [By.XPATH, locators.input_metro_list]
    input_metro_station = [By.XPATH, locators.input_metro_station]
    phone_number = [By.XPATH, locators.input_phone_number_field]
    button_order_next = [By.XPATH, locators.button_order_form_next]
    input_date = [By.XPATH, locators.input_date_field]
    input_rent_term_field = [By.XPATH, locators.input_rent_term_field]
    input_rent_term_item = [By.XPATH, locators.input_rent_term_list_item]
    input_color_checkbox = [By.XPATH, locators.input_color_checkbox]
    input_comment_field = [By.XPATH, locators.input_comment_field]
    button_order_form_back = [By.XPATH, locators.button_order_form_back]
    button_order_form_order = [By.XPATH, locators.button_order_form_order]
    header_order_confirmation = [By.XPATH, locators.header_order_confirmation]
    button_order_confirmation_yes = [By.XPATH, locators.button_order_confirmation_yes]
    header_completed_order_confirmation = [By.XPATH, locators.header_completed_order_confirmation]
    button_completed_order_status_check = [By.XPATH, locators.button_completed_order_status_check]
    button_order_details_cancel = [By.XPATH, locators.button_order_details_cancel]
    header_logo_yandex = [By.XPATH, locators.header_logo_yandex]
    header_logo_scooter = [By.XPATH, locators.header_logo_scooter]
    order_button_main = [By.XPATH, locators.order_button_main]


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажатие на кнопку Принять Куки')
    def accept_cookies_button(self):
        self.driver.find_element(*self.accept_cookies_yes).click()

    @allure.step('Заполнение поля Имя')
    def set_name(self, name):
        self.driver.find_element(*self.input_name).send_keys(name)

    @allure.step('Заполнение поля Фамилия')
    def set_surname(self, surname):
        self.driver.find_element(*self.input_surname).send_keys(surname)

    @allure.step('Заполнение поля Адрес')
    def set_address(self, address):
        self.driver.find_element(*self.input_address).send_keys(address)

    @allure.step('Выбор станции метро')
    def set_metro_station(self, station):
        self.driver.find_element(*self.metro_list).click()
        option_locator = (self.input_metro_station[0], self.input_metro_station[1].format(option=station))
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(option_locator))
        self.driver.find_element(*option_locator).click()

    @allure.step('Заполнение поля Телефон')
    def set_telephone_number(self, phone):
        self.driver.find_element(*self.phone_number).send_keys(phone)

    @allure.step('Нажатие на кнопку Далее')
    def click_button_next(self):
        self.driver.find_element(*self.button_order_next).click()

    @allure.step('Заполнение поля Дата резервации')
    def set_date(self, date):
        self.driver.find_element(*self.input_date).send_keys(date)

    @allure.step('Выбор срока аренды из выпадающего списка')
    def set_term(self, term):
        self.driver.find_element(*self.input_rent_term_field).click()
        term_locator = (self.input_rent_term_item[0], self.input_rent_term_item[1].format(term=term))
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(term_locator))
        self.driver.find_element(*term_locator).click()

    @allure.step('Выбор цвета скутера(активация чекбокса)')
    def select_scooter_color(self, color):
        checkbox_locator = (self.input_color_checkbox[0], self.input_color_checkbox[1].format(color=color))
        self.driver.find_element(*checkbox_locator).click()

    @allure.step('Заполнение поля Комментарий')
    def set_comment(self, comment):
        self.driver.find_element(*self.input_comment_field).send_keys(comment)

    @allure.step('Нажатие на кнопку Заказать')
    def click_order_button(self):
        self.driver.find_element(*self.button_order_form_order).click()
        #WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.header_order_confirmation))

    @allure.step('Нажатие на кнопку ДА в окне подтверждения заказа')
    def click_order_confirmation_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.header_order_confirmation))
        self.driver.find_element(*self.button_order_confirmation_yes).click()

    @allure.step('Нажатие на кнопку "Посмотреть детали"')
    def click_button_check_status_on_confirmation(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.header_completed_order_confirmation))
        self.driver.find_element(*self.button_completed_order_status_check)

    @allure.step('Нажатие на Логотип Самокат в шапке ')
    def click_header_logo_scooter(self):
        self.driver.find_element(*self.header_logo_scooter).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.order_button_main))

    @allure.step('Нажатие на логотип Яндекс в шапке для перехода на Дзен')
    def click_header_logo_yandex(self):
        self.driver.find_element(*self.header_logo_yandex).click()

    @allure.step('Ожидание открытия Дзен в новом окне')
    def wait_for_new_window_and_switch(self):
        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened)
        new_window = [window for window in self.driver.window_handles if window != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window)

    @allure.step('Проверка что переход на Дзен осуществлён')
    def verify_url(self):
        expected_url = "https://dzen.ru/?yredirect=true"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url, f"Expected URL {expected_url}, but got {self.driver.current_url}"

