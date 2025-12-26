import allure
from data import OrderAnswer
from pages.main_page import MainPage
import pytest


class TestMainPage:

    @pytest.mark.parametrize(
        "question_number,answer_number,expected_answer",
        [(0, 0, OrderAnswer.ANSWER_1), (1, 1, OrderAnswer.ANSWER_2), (2, 2, OrderAnswer.ANSWER_3),
         (3, 3, OrderAnswer.ANSWER_4), (4, 4, OrderAnswer.ANSWER_5), (5, 5, OrderAnswer.ANSWER_6),
         (6, 6, OrderAnswer.ANSWER_7), (7, 7, OrderAnswer.ANSWER_8)]
    )

    @allure.step("Проверяем соответствие ответа и вопроса в выпадающем опроснике")
    def test_faq_answer_question(self, driver, question_number, answer_number, expected_answer):
        page = MainPage(driver)
        page.open()
        page.cookie_click()
        page.question_click(question_number)
        text = page.answer_text(answer_number)
        assert text == expected_answer
