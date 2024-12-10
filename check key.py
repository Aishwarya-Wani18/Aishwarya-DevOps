# Python Program to Check if a Given Key Exists in a Dictionary or Not 
dict = {'name': 'Aishwarya', 'roll_number': 121, 'Address': 'Aurangabad', 'percentage': '95%', 'Category': 'Open'}
check_key = input("Enter key to check data: ")
for key in dict:
    if check_key == key:
        print("key is present")
        break
else:
    print("Key is not present")