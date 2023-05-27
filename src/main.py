import datetime
from classes import Output
from get_data import sort_data_executed

def sortFunction(data):
    """Функция преобразования из isoformat в дату"""
    return datetime.datetime.fromisoformat(data["date"])

data = sort_data_executed()  # вывод значения даты из функции sortFunction

data.sort(key=sortFunction, reverse=True)  # сортировка по дате


def output_data_func(value):
    output_data = []
    number_of_index = 0
    for i in data[0:value]:
        output_data.append(i)
        operation = Output(output_data[number_of_index].get("date"), output_data[number_of_index].get("description"), output_data[number_of_index].get("operationAmount"), output_data[number_of_index].get("from"), output_data[number_of_index].get("to"))
        operation.print_1th_string()
        operation.print_2th_string()
        operation.print_3th_string()
        number_of_index += 1
    return output_data

output_data = output_data_func(5)
