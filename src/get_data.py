import json
from datetime import datetime


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


#def sortFunction(data):
    #return datetime.datetime.fromisoformat(data["date"])

#data = sort_data_executed()

#data.sort(key=sortFunction, reverse=True)
#print(data)


#d = datetime.datetime.fromisoformat('2019-08-26T10:50:58.294041')
#print(d)
#print(type(d))

