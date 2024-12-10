# Python Program to Add a Key-Value Pair to the Dictionary


def key_value(data):
    dic1 = {}
    for kv in range(data):
        key = input("Enter key: ")
        value = input("Enter vslue: ")
        dic1[key] = value
    return dic1

data = int(input("How many Key paie you want:"))
dictionary = key_value(data)
print(dictionary)