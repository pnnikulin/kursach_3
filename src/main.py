import datetime
from datetime import date

from get_data import sort_data_executed

def sortFunction(data):
    return datetime.datetime.fromisoformat(data["date"])

data = sort_data_executed()

data.sort(key=sortFunction, reverse=True)
#print(data[0:5])

class Output:
    def __init__(self, date, description, operationAmount, from_, to):
        self.date = date
        self.description = description
        self.operationAmount = operationAmount
        self.from_ = from_
        self.to = to

    def print_1th_string(self):
        date_only = datetime.datetime.fromisoformat(self.date).date().strftime("%Y.%m.%d")
        print(f"{date_only} {self.description}")

    def print_2th_string(self):
       print(f"{self.from_}")


def output_data_func(value):
    output_data = []
    number_of_index = 0
    for i in data[0:value]:
        output_data.append(i)
        number_of_index +=1
        operation_1 = Output(output_data[number_of_index].get("date"), output_data[number_of_index].get("description"), output_data[number_of_index].get("operationAmount"), output_data[number_of_index].get("from"), output_data[number_of_index].get("to"))
        operation_1.print_1th_string()
        operation_1.print_2th_string()

    return output_data

output_data = output_data_func(4)




operation_1 = Output(data[0]["date"], data[0]["description"], data[0]["operationAmount"], data[0].get("from"), data[0]["to"])
operation_1.print_1th_string()
operation_1.print_2th_string()