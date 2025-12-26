from locators.dzen_page_locators import DzenLocators
from pages.base_page import BasePage
from tests.conftest import driver


class DzenPage(BasePage):
    def is_logo_visible(self):
       return self.wait_and_find_element(DzenLocators.LOGO_DZEN).is_displayed()

    def get_current_url(self):
        return self.driver.current_url