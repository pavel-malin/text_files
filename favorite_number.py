import json

#favorite_number = input("Favorite number? ")
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

# with open(filename, 'w') as f_obj:
#    json.dump(favorite_number, f_obj)
#    print("I know your favorite numbers is " + favorite_number + "!")