from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import data
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
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


    def set_adress_input(self, adress):
        self.send_keys(OrderPageLocators.ADRESS_INPUT, adress)

    #def set_station_select(self,subway_name ):
        #return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]

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

    def click_order_button(self):
        self.wait_and_click(OrderPageLocators.NEXT_BUTTON)

    def previos_button_is_displayed(self):
        self.wait_and_find_element(OrderPageLocators.PREVIOUS_BUTTON)

    def set_date_input(self, date):
        date_input = self.wait_and_find_element(OrderPageLocators.WHEN_INPUT)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    def set_time_input(self, time):
        # открыть дропдаун
        dropdown = self.wait_and_find_element(OrderPageLocators.TIME_DROPDOWN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()

        # выбрать первый доступный вариант
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.TIME_OPTION)
        )
        option.click()

    def set_color_input(self, color):
        color_checkbox = self.wait_and_find_element(OrderPageLocators.COLOR_CHECKBOX)
        color_checkbox.send_keys(Keys.ENTER)

    def send_comment(self,comment):
        self.send_keys(OrderPageLocators.COMMENT,comment)

    def order_completed(self):
        text_order_completed= self.get_text(OrderPageLocators.ORDER_COMPLETED)
        return text_order_completed



