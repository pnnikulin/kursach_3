import json


def load_data():
    """Функция получения данных из файла operation.json"""
    with open("src/operations.json", "r", encoding='utf-8') as file:
        data_json = file.read()
        data = json.loads(data_json)
    return data


def sort_data_executed():
    """Функция отбора данных по полю EXECUTED"""
    data = load_data()
    data_sorted_executed = []
    for i in data:
        if i["state"] == "EXECUTED":
            data_sorted_executed.append(i)
    return data_sorted_executed