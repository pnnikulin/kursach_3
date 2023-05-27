import json


def load_data():
    with open("operations.json", "r") as file:
        data_json = file.read()
        data = json.loads(data_json)
    return data


def sort_data_executed():
    data = load_data()
    data_sorted_executed = []
    for i in data:
        if i["state"] == "EXECUTED":
            data_sorted_executed.append(i)
    return data_sorted_executed