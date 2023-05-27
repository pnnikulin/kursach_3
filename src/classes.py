import datetime
import re

class Output:
    def __init__(self, date, description, operationAmount, from_, to):
        self.date = date
        self.description = description
        self.operationAmount = operationAmount
        self.from_ = from_
        self.to = to

    def print_1th_string(self):
        """Первая строка вывода"""
        date_only = datetime.datetime.fromisoformat(self.date).date().strftime("%Y.%m.%d")
        print(f"{date_only} {self.description}")

    def print_2th_string(self):
        """Вторая строка вывода"""
        if self.from_ == None:
            pass

        elif "Счет" in self.from_ and "Счет" in self.to:  #From и To имеют значение "Счёт"
            print(f"{re.sub('[^A-Za-zА-Яа-я ]', '', self.from_)} **{self.from_.replace(' ', '')[-4:]} -> {re.sub('[^A-Za-zА-Яа-я ]', '', self.to)} **{self.to.replace(' ', '')[-4:]}")  # Example: -> Счет **9937 -> -> Счет **9638

        elif "Счет" in self.from_:  #From имеют значение "Счёт"
            print(f"{re.sub('[^A-Za-zА-Яа-я ]', '', self.from_)} **{self.from_.replace(' ', '')[-4:]} -> {re.sub('[^A-Za-zА-Яа-я ]', '', self.to)} {self.to.replace(' ', '')[-16:-12]} {self.to.replace(' ', '')[-12:-10]}** **** {self.to.replace(' ', '')[-4:]}")  # Example: Счет **9638 -> Visa Platinum 7000 79** **** 6361

        elif "Счет" in self.to:  #To имеют значение "Счёт"
            print(f"{re.sub('[^A-Za-zА-Яа-я ]', '', self.from_)} {self.from_.replace(' ', '')[-16:-12]} {self.from_.replace(' ', '')[-12:-10]}** **** {self.from_.replace(' ', '')[-4:]} -> {re.sub('[^A-Za-zА-Яа-я ]', '', self.to)} **{self.to.replace(' ', '')[-4:]}")  # Example: Visa Platinum 7000 79** **** 6361 -> Счет **9638

        else:   #Поля не имеют значение "Счёт"
            print(f"{re.sub('[^A-Za-zА-Яа-я ]', '', self.from_)} {self.from_.replace(' ', '')[-16:-12]} {self.from_.replace(' ', '')[-12:-10]}** **** {self.from_.replace(' ', '')[-4:]} -> {re.sub('[^A-Za-zА-Яа-я ]', '', self.to)} {self.to.replace(' ', '')[-16:-12]} {self.to.replace(' ', '')[-12:-10]}** **** {self.to.replace(' ', '')[-4:]}")  # Example: Visa Platinum 7000 79** **** 6361 -> Visa Platinum 7000 79** **** 6361

    def print_3th_string(self):
        print(f"{self.operationAmount['amount']} {self.operationAmount['currency']['name']}\n")


#Maestro 7810 8465 9678 5568

# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.