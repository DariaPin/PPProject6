from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Config
from data import OrderPageTestData
import time


import data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    URL = data.Urls.ORDER_PAGE
    def open(self):
        self.driver.get(self.URL)

    def set_name_input(self,name):
        self.send_keys(OrderPageLocators.NAME_INPUT,name)

    def set_lastname_input(self, lastname):
        self.send_keys(OrderPageLocators.LASTNAME_INPUT,lastname)

    def wait_and_find_element_order_button(self):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(OrderPageTestData.ORDER_BUTTON))
        return self.driver.find_element(*OrderPageTestData.ORDER_BUTTON)

    def wait_and_find_element_when_input(self,calendar):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(OrderPageLocators.WHEN_INPUT))
        #self.driver.find_element(*OrderPageLocators.WHEN_INPUT).click()
        self.send_keys(OrderPageLocators.WHEN_INPUT,calendar)


    def set_adress_input(self, adress):
        self.send_keys(OrderPageLocators.ADRESS_INPUT, adress)


    def set_station_select(self, station_name):
        station_input = self.wait_and_find_element(OrderPageLocators.STATION_INPUT)
        station_input.send_keys(station_name)

        station_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='{station_name}']")
            )
        )
        station_option.click()

    def set_phone_input(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    def previos_button_is_displayed(self):
        self.wait_and_find_element(OrderPageLocators.PREVIOUS_BUTTON)

    def set_date_input(self):
        date_input = self.wait_and_find_element(OrderPageLocators.WHEN_INPUT)
        date_input.send_keys(OrderPageTestData.DATE)
        date_input.send_keys(Keys.ENTER)

    def set_date_input_date(self, date):
        date_input = self.wait_and_find_element(OrderPageLocators.WHEN_INPUT)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)


    def set_time_input_time(self):
        # открыть дропдаун
        dropdown = self.wait_and_find_element(OrderPageLocators.TIME_DROPDOWN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()
        # выбрать первый доступный вариант
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.TIME_OPTION)
        )
        option.click()

    def set_color(self, color):
        if color == "чёрный жемчуг":
            self.click_js(OrderPageLocators.BLACK_SCOOTER)
        elif color == "серая безысходность":
            self.click_js(OrderPageLocators.GREY_SCOOTER)

    def send_comment_data(self,comment_data):
        self.send_keys(OrderPageLocators.COMMENT,comment_data)

    def order_completed(self):
        text_order_completed= self.get_text(OrderPageLocators.ORDER_COMPLETED)
        return text_order_completed

    def click_samokat_button(self):
        self.wait_and_click(OrderPageLocators.SAMOKAT_LINK)

    def profile_title_is_displayed(self):
         boolean_profile_title_is_displayed = self.wait_for_presence(OrderPageLocators.PROFILE_NAME)
         return boolean_profile_title_is_displayed

    def profile_title_get_text(self):
        profile_name_main = self.wait_and_find_element(OrderPageLocators.PROFILE_NAME)

    def safe_click_yandex_logo(self):
        self.safe_click(OrderPageLocators.YANDEX_LOGO)

    def cookie_banner_method(self):
        try:
            cookie_banner = self.wait_and_find_element(OrderPageLocators.COOKIE)
            if cookie_banner:
                close_button = cookie_banner.find_element(*OrderPageLocators.COOKIE_BUTTON)
                close_button.click()
        except TimeoutException:

            pass

    def click_order_button(self):
        wait = WebDriverWait(self.driver, 5)
        next_button = wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        next_button.click()

    def close_cookie_banner(self):
        """Закрываем баннер cookie, если он видим"""
        try:
            wait = WebDriverWait(self.driver, 5)
            cookie_close_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".App_CookieButton__1y7iE"))
            )
            cookie_close_btn.click()
            wait.until(EC.invisibility_of_element(cookie_close_btn))  # ждём пока скроется
        except:
            pass  # если баннера нет — просто продолжаем

    def set_station_select(self, station_name):
        """Выбираем станцию из списка"""
        self.close_cookie_banner()  # теперь точно закрываем баннер

        station_input = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.STATION_INPUT)
        )
        station_input.click()

        station_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='{station_name}']")
            )
        )
        station_option.click()

    def click_place_order_button(self):
        self.click_js(OrderPageLocators.PLACE_ORDER_BUTTON)

    def click_place_order_yes_button(self):
        self.click_js(OrderPageLocators.YES_BUTTON)
