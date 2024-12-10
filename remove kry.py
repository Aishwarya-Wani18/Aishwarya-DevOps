# Python Program to Remove the Given Key from a Dictionary

dict = {'a': 12, 'b': 15, 'c': 7, 'd': 18, 'e': 40}
remove_key = input("Which Data You want to remove: ")

if remove_key in dict:
    del dict[remove_key]
else:
    print("Key is not present in dictionary")

print(dict)