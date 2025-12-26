from selenium.webdriver.common.by import By


class Urls:

    SAMOKAT_URL='https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'

class DzenUrls:
    DZEN_URL = 'https://dzen.ru/?yredirect=true'

class Config:
    DEFAULT_TIMEOUT =   15


class OrderAnswer:
    ANSWER_1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    ANSWER_2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    ANSWER_3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ANSWER_4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    ANSWER_5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    ANSWER_6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    ANSWER_7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    ANSWER_8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

class OrderPageTestData:
    ORDER_BUTTON = (By.XPATH, "//button[@class = 'Button_Button__ra12g']")
    NAME = 'Дарья'
    LAST_NAME = 'Пинчук'
    ADRESS = 'улица Ленина 1'
    STATION = 'Жулебино'
    PHONE = '79266667788'
    DATE = '17.09.2026'
    TIME = 'сутки'
    COLOR = 'черный жемчуг'
    COMMENT_DATA = 'любой кмментарий'

    ORDER_BUTTON1 = (By.XPATH, "//button[@class = 'Button_Button__ra12g']")
    NAME1 = 'Марья'
    LAST_NAME1 = 'Иванова'
    ADRESS1 = 'улица Ленина 2'
    STATION1 = 'Выхино'
    PHONE1 = '79266667789'
    DATE1 = '12.10.2026'
    TIME1 = 'сутки'
    COLOR1 = 'черный жемчуг'
    COMMENT_DATA1 = 'любой кмментарий'







class DzenPageTestData:
    DZEN_LOGIN_BUTTON = 'Войти'


