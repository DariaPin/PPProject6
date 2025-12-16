from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Config

import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    @allure.step('Подождать и найти элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Подождать и кликнуть')
    def wait_and_click(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    @allure.step('Подождать и отправить текст')
    def send_keys(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    @allure.step('Получить текст')
    def get_text(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text

    @allure.step('Проскроллить до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def wait_for_presence(self, locator):
        return WebDriverWait(
            self.driver, Config.DEFAULT_TIMEOUT
        ).until(EC.presence_of_element_located(locator))

    def click_js(self, locator):
        element = self.wait_for_presence(locator)
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)

    def safe_click(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except TimeoutException:
            pass
