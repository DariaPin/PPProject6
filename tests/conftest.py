import pytest
from selenium import webdriver

import data
from data import Urls
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()# или Chrome
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    driver.get(data.Urls.SAMOKAT_URL)  # URL для главной страницы
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    driver.get(data.Urls.ORDER_PAGE)  # URL для страницы заказа
    return page