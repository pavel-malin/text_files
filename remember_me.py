import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    while True:
        user = input("What is you name? ")
        name = input("Did you spell your name right? (yes/no) ")
        if name == 'no':
            continue
        if name == 'yes':
            filename = 'username.json'
            with open(filename, 'w') as f_obj:
                json.dump(user, f_obj)
            return user

def greet_user():
    user = get_new_username()
    if user in filename:
        username = get_stored_username()
        print("Welcome back, " + username + "!")
    if user not in filename:
        username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")

# user = input("What is you name? ")
filename = 'username.json'
greet_user()