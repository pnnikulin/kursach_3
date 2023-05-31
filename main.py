import datetime
from src.classes import Output
from src.get_data import sort_data_executed

def sortFunction(data):
    """Функция преобразования из isoformat в дату"""
    return datetime.datetime.fromisoformat(data["date"])


data = sort_data_executed()  # вывод значения даты из функции sortFunction


data.sort(key=sortFunction, reverse=True)  # сортировка по дате


def main(value):
    """Основная функция для создания экземпляров класса (5 последних операций)"""
    output_data = []
    number_of_index = 0
    for i in data[0:value]:
        output_data.append(i)
        operation = Output(output_data[number_of_index].get("date"), output_data[number_of_index].get("description"),
                           output_data[number_of_index].get("operationAmount"),
                           output_data[number_of_index].get("from"), output_data[number_of_index].get("to"))
        print(operation.print_1th_string())
        print(operation.print_2th_string())
        print(operation.print_3th_string())
        number_of_index += 1
    return output_data


if __name__ == "__main__":
    main(5)

