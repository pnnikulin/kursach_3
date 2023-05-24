import datetime
from datetime import date

from get_data import sort_data_executed

def sortFunction(data):
    return datetime.datetime.fromisoformat(data["date"])

data = sort_data_executed()

data.sort(key=sortFunction, reverse=True)
print(data[0:5])

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


operation_1 = Output(data[1]["date"], data[1]["description"], data[1]["operationAmount"], data[1]["from"], data[1]["to"])
operation_1.print_1th_string()
operation_1.print_2th_string()