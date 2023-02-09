from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from pytest import raises
from unittest.mock import patch

input_mock = [
    {
        "title": "Noticia Mock 01",
        "reading_time": 8,
    },
    {
        "title": "Noticia Mock 02",
        "reading_time": 7,
    },
    {
        "title": "Noticia Mock 03",
        "reading_time": 20,
    },
    {
        "title": "Noticia Mock 04",
        "reading_time": 15,
    },
]

readable_mock = [
    {"chosen_news": [("Noticia Mock 01", 8)], "unfilled_time": 2},
    {"chosen_news": [("Noticia Mock 02", 7)], "unfilled_time": 3},
]

unreadable_mock = [('Noticia Mock 03', 20), ('Noticia Mock 04', 15)]


def test_reading_plan_group_news():
    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=input_mock
    ):
        news = ReadingPlanService.group_news_for_available_time(10)
        assert news["readable"] == readable_mock
        assert news["unreadable"] == unreadable_mock
    with raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        news = ReadingPlanService.group_news_for_available_time(0)
