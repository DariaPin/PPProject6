from calendar import calendar

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.order_page import OrderPage
from data import OrderPageTestData
from pages.main_page import MainPage
from data import Urls
from locators.order_page_locators import OrderPageLocators
from tests.conftest import order_page
import time
from pages.order_page import OrderPage


#class TestOrderPage:

    # def test_correct_fill_in(self, driver):
    #     order_page = OrderPage(driver)
    #     order_page.open()
    #     #cookie_banner = driver.find_elements(*OrderPageLocators.COOKIE)
    #     #if cookie_banner:
    #         #close_button = cookie_banner[0].find_element(*OrderPageLocators.ORDER_BUTTON)  # обычно есть кнопка закрытия
    #         #close_button.click()
    #     order_page.cookie_banner_method()
    #     order_page = OrderPage(driver)
    #     order_page.wait_and_find_element(OrderPageTestData.ORDER_BUTTON)
    #     order_page.set_name_input(OrderPageTestData.NAME)
    #     order_page.set_lastname_input(OrderPageTestData.LAST_NAME)
    #     order_page.set_phone_input(OrderPageTestData.PHONE)
    #     order_page.set_adress_input(OrderPageTestData.ADRESS)
    #     order_page.set_station_select(OrderPageTestData.STATION)
    #     order_page.click_order_button()
    #     order_page.wait_and_find_element(OrderPageLocators.WHEN_INPUT)
    #     order_page.set_date_input(OrderPageTestData.DATE)
    #     order_page.set_time_input(OrderPageTestData.TIME)
    #     order_page.send_comment(OrderPageTestData.COMMENT_DATA)
    #     order_page.click_js(OrderPageLocators.PLACE_ORDER_BUTTON)
    #     order_page.click_js(OrderPageLocators.YES_BUTTON)

        #assert "Заказ оформлен" in order_page.order_completed()
#order_page.click_js(*OrderPageLocators.STATUS)


class TestOrderPage:
    @pytest.mark.parametrize(
        "name, last_name, phone, address, station, calendar, date, color, comment_data",
        [
            ("Анна", "Иванова", "89990000001", "Москва, Ленина 1", "Черкизовская","17.06.2026","сутки","чёрный жемчуг","коммент1"),
            ("Иван", "Петров", "89990000002", "Москва, Тверская 5", "Тверская",  "17.09.2026","сутки","чёрный жемчуг","коммент2")
        ]
    )
    def test_correct_fill_in(
        self, driver, name, last_name, phone, address,calendar, station, date, color, comment_data
    ):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.cookie_banner_method()
        order_page.wait_and_find_element_order_button()
        order_page.set_name_input(name)
        order_page.set_lastname_input(last_name)
        order_page.set_phone_input(phone)
        order_page.set_adress_input(address)
        order_page.set_station_select(station)

        order_page.click_order_button()
        order_page.wait_and_find_element_when_input(calendar)

        order_page.set_date_input_date(date)
        order_page.set_time_input_time()
        order_page.send_comment_data(comment_data)
        #order_page.set_color_input(color)
        order_page.set_color(color)

        order_page.click_place_order_button()
        order_page.click_place_order_yes_button()

        assert "Заказ оформлен" in order_page.order_completed()

    def test_samokat_link_open_main_page(self,driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_samokat_button()
        time.sleep(5)
        assert order_page.profile_title_is_displayed()





