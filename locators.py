# A locators list of https://qa-scooter.praktikum-services.ru/

accept_cookies_button = './/button[text()="да все привыкли"]'
# 1st part of order form
input_name_field = './/div/input[@placeholder="* Имя"]'
input_surname_field = './/div/input[@placeholder="* Фамилия"]'
input_address_field = './/div/input[@placeholder="* Адрес: куда привезти заказ"]'
input_metro_list = './/div/input[@placeholder="* Станция метро"]'
input_metro_station = './/li/button/div[text()="{option}"]'
input_phone_number_field = './/div/input[@placeholder="* Телефон: на него позвонит курьер"]'
button_order_form_next = './/div/button[text()="Далее"]'

# 2nd part of order form
input_date_field = './/div/input[@placeholder="* Когда привезти самокат"]'
input_rent_term_field = './/div/span[@class="Dropdown-arrow"]'
input_rent_term_list_item = './/div[text()="{term}"]'
input_color_checkbox = './/label/input[@id="{color}"]'
input_comment_field = './/div/input[@placeholder="Комментарий для курьера"]'
button_order_form_back = './/button[text()="Назад"]'
button_order_form_order = './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'

# order confirmation modal window
header_order_confirmation = './/div[text()="Хотите оформить заказ?"]'
button_order_confirmation_yes = './/button[text()="Да"]'

# successful order modal window
header_completed_order_confirmation = './/div[text()="Заказ оформлен"]'
button_completed_order_status_check = './/button[text()="Посмотреть статус"]'

# completed order track
button_order_details_cancel = './/button[text()="Отменить заказ"]'

# main header of the site
header_logo_yandex = './/div[@class="Header_Logo__23yGT"]/a[@class="Header_LogoYandex__3TSOI"]'
header_logo_scooter = './/div/a[@class="Header_LogoScooter__3lsAR"]'
header_order_button = './/div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]'

# main page
order_button_main = './/div[@class="Home_FinishButton__1_cWm"]/button'

# Вопросы о важном
# Сколько это стоит и как оплатить?
header_faq = './/div[text()="Вопросы о важном"]'
question1 = './/div[text()="Сколько это стоит? И как оплатить?"]'
answer1 = './/div/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]'
question2 = './/div[text()="Хочу сразу несколько самокатов! Так можно?"]'
answer2 = './/div/p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]'
question3 = './/div[text()="Как рассчитывается время аренды?"]'
answer3 = './/div/p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]'
question4 = './/div[text()="Можно ли заказать самокат прямо на сегодня?"]'
answer4 = './/div/p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]'
question5 = './/div[text()="Можно ли продлить заказ или вернуть самокат раньше?"]'
answer5 = './/div/p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]'
question6 = './/div[text()="Вы привозите зарядку вместе с самокатом?"]'
answer6 = './/div/p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]'
question7 = './/div[text()="Можно ли отменить заказ?"]'
answer7 = './/div/p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]'
question8 = './/div[text()="Я жизу за МКАДом, привезёте?"]'
answer8 = './/div/p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]'
