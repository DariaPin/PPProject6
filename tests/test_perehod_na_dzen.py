import allure

from pages.dzen_page import DzenPage
from pages.order_page import OrderPage
from data import OrderPageTestData, DzenUrls

class Test_Dzen_Page:

    @allure.epic("Переходы по внешним ссылкам")
    @allure.feature("Яндекс → Дзен")
    @allure.story("Переход на страницу Дзена по логотипу")
    @allure.title("Переход на Дзен по клику на логотип Яндекса")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_dzen_link_redirect(self, driver):
        order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу Самоката"):
            order_page.open()

        with allure.step("Нажать на логотип Яндекса"):
            order_page.safe_click_yandex_logo()

        with allure.step("Переключиться на новую вкладку"):
            order_page.switch_window()

        dzen_page = DzenPage(driver)

        with allure.step("Проверить, что логотип Дзена отображается"):
            assert dzen_page.is_logo_visible()

        with allure.step("Проверить, что URL соответствует странице Дзена"):
            assert dzen_page.get_current_url() == DzenUrls.DZEN_URL
