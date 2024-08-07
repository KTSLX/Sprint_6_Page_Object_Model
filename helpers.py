import random as r
import datetime as d

street = ['Косая аллея 5', 'Косой переулок 12', 'Диагон аллея 5']

metro = ['Бульвар Рокоссовского', 'Речной вокзал', 'Пятницкое шоссе', 'Кунцевская', 'Медведково', 'Планерная',
         'Раменки', 'Алтуфьево', 'Петровско-Разумовская', 'Каширская', 'Битцевский парк', 'Окружная']

period = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']

color = ['чёрный жемчуг', 'серая безысходность']

def tomorrow():
    today = d.date.today()
    tomorrow = today + d.timedelta(days=1)
    return tomorrow.strftime('%d.%m.%y')


class OrderData:
    name = 'Александр'
    surname = 'Крутой'
    address = r.choice(street)
    metro = r.choice(metro)
    phone = r.randint(70000000000, 79999999999)
    day = tomorrow()
    period = r.choice(period)
    color = r.choice(color)
    comment = 'Не звонить в домофон'