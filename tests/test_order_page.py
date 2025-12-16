import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.order_page import OrderPage
from data import OrderPageTestData
from pages.main_page import MainPage
from data import Urls
from locators.order_page_locators import OrderPageLocators
from tests.conftest import order_page


class TestOrderPage:

    def test_correct_fill_in(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        cookie_banner = driver.find_elements(By.CLASS_NAME, "App_CookieConsent__1yUIN")
        if cookie_banner:
            close_button = cookie_banner[0].find_element(By.TAG_NAME, "button")  # обычно есть кнопка закрытия
            close_button.click()
        order_page = OrderPage(driver)
        order_page.wait_and_find_element(OrderPageTestData.ORDER_BUTTON)
        order_page.set_name_input(OrderPageTestData.NAME)
        order_page.set_lastname_input(OrderPageTestData.LAST_NAME)
        order_page.set_phone_input(OrderPageTestData.PHONE)
        order_page.set_adress_input(OrderPageTestData.ADRESS)
        order_page.set_station_select(OrderPageTestData.STATION)
        order_page.click_order_button()
        order_page.wait_and_find_element(OrderPageLocators.WHEN_INPUT)
        order_page.set_date_input(OrderPageTestData.DATE)
        order_page.set_time_input(OrderPageTestData.TIME)
        order_page.send_comment(OrderPageTestData.COMMENT_DATA)
        order_page.click_js(OrderPageLocators.PLACE_ORDER_BUTTON)
        order_page.click_js(OrderPageLocators.YES_BUTTON)

        assert "Заказ оформлен" in order_page.order_completed()

        order_page.click_js(OrderPageLocators.STATUS)


