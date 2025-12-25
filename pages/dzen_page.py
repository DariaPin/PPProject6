from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data
from data import Urls
from locators.dzen_page_locators import DzenLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class DzenPage(BasePage):
    def is_logo_visible(self):
       return self.wait_and_find_element(DzenLocators.LOGO_DZEN).is_displayed()