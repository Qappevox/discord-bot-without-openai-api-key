import json
def getter(index):
    with open('API.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
        print(data[index])
        return data[index]
  
def setter(index, val):
    with open('API.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    data[index] = val
    with open('API.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
