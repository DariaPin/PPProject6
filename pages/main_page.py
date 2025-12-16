from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    URL = data.Urls.SAMOKAT_URL

    def open(self):
        self.driver.get(self.URL)

    def cookie_click(self):
        self.safe_click(MainPageLocators.COOKIE_BUTTON)

    def answer_text(self, answer_number):
        locator = MainPageLocators.faq_answer_text(answer_number)

        element = WebDriverWait(self.driver, 10).until(
            lambda driver: (
                               el := driver.find_element(*locator)
                           ) and el.text.strip()
        )

        return element

    def question_click(self, question_number):
        locator = MainPageLocators.faq_question_button(question_number)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        self.driver.execute_script("arguments[0].click();", element)

