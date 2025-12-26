import pytest
import time
from pages.order_page import OrderPage


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





