from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    DZEN_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

   # @staticmethod
    #def faq_question_button(question_number):
       # """Возвращает локатор кнопки с вопросом FAQ (нумерация сверху вниз)"""
       # return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]

   # @staticmethod
    #def faq_answer_text(answer_number):
        #return [By.XPATH, f".//div[@class='accordion__button' and @id = 'accordion__panel-{answer_number}']"]


    @staticmethod
    def faq_question_button(number):
        return (By.ID, f"accordion__heading-{number}")

    @staticmethod
    def faq_answer_panel(number):
        return (By.ID, f"accordion__panel-{number}")

    @staticmethod
    def faq_answer_text(number):
        return (
            By.XPATH,
            f"//div[@id='accordion__panel-{number}']//p"
        )