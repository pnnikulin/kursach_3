import pytest

from src.classes import Output


@pytest.fixture
def output_object():
    date = "2019-12-07T06:17:14.634890"
    description = "Перевод организации"
    operationAmount = {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}
    from_ = "Visa Classic 2842878893689012"
    to = "Счет 35158586384610753655"
    return Output(date, description, operationAmount, from_, to)


def test_1st_string(output_object):
    assert output_object.print_1th_string() == "07.12.2019 Перевод организации"


def test_2st_string(output_object):
    assert output_object.print_2th_string() == "Visa Classic  2842 87** **** 9012 -> Счет  **3655"


def test_3st_string(output_object):
    assert output_object.print_3th_string() == "48150.39 USD\n"


@pytest.fixture
def output_object_None():
    date = "2019-12-07T06:17:14.634890"
    description = "Перевод организации"
    operationAmount = {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}
    from_ = None
    to = "Счет 35158586384610753655"
    return Output(date, description, operationAmount, from_, to)


def test_2st_string_None(output_object_None):
    assert output_object_None.print_2th_string() == "*"