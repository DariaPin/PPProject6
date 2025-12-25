import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.dzen_page import DzenPage
from pages.order_page import OrderPage
from data import OrderPageTestData, DzenUrls
from pages.main_page import MainPage
from data import Urls
from locators.order_page_locators import OrderPageLocators
from tests.conftest import order_page

class Test_Dzen_Page:
    def test_dzen_link_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.safe_click_yandex_logo()
        order_page.switch_window()
        dzen_page = DzenPage(driver)

        assert dzen_page.is_logo_visible()
        assert driver.current_url == DzenUrls.DZEN_URL