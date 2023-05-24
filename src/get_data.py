import json

#with open("operations.json", "r") as file:
    #data_json = file.read()
    #data = json.dumps(data_json, indent=2)


def load_data():
    with open("operations.json", "r") as file:
        data_json = file.read()
        data = json.loads(data_json)
        return data

data = load_data()
print(len(data))
print(type(data))
print(data)


def sort_data_executed():
    load_data()
    data_sorted_executed = []
    for i in data:
        if i["state"] == "EXECUTED":
            data_sorted_executed.append(i)
    return data_sorted_executed


print(sort_data_executed())
print(len(sort_data_executed()))


#def sortFunction(element):
    #return element["state"] == 'EXECUTED'



#sortFunction()
#result = data.sort(key=sortFunction)
#print(result)

