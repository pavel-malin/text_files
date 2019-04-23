# Asks for a favorite number, if the number in the list is not present,
# it overwrites and displays a new favorite number.
import json

filename = 'favorite_number.json'
try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
        number = input("Favorite number? ")
except FileNotFoundError:
    if number in favorite_number:
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj)
else:
    print("I know your favorite numbers is " + number + "!")