from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_BUTTON = (By.XPATH, "//button[@class = 'Button_Button__ra12g']")
    NEXT_BUTTON = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    PREVIOUS_BUTTON = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder = '* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    ADRESS_INPUT = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    STATION_INPUT = (By.XPATH,"//input[@placeholder = '* Станция метро']")
    WHEN_INPUT = (By.XPATH, "//input[@placeholder= '* Когда привезти самокат']")
    TIME_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    TIME_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    TIME_INPUT = (By.XPATH,"//div[@class= 'Dropdown-arrow-wrapper']")
    COLOR_CHECKBOX = (By.XPATH, "//div[@class= 'Order_Checkboxes__3lWSI']")
    BLACK_SCOOTER = (By.XPATH, "//input[@id='black']")
    GREY_SCOOTER = (By.XPATH, "//input[@id='grey']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    PLACE_ORDER_BUTTON = (By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    YES_BUTTON = (By.XPATH,"//button[normalize-space(text())='Да']")
    ORDER_COMPLETED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    STATUS = (By.XPATH, "//button[normalize-space(text())='Посмотреть статус']")
