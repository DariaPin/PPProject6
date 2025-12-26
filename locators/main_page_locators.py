from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    DZEN_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")


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