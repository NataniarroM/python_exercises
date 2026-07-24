import json
def greet_user():
    "It greets the user with his own name, confirming first if the username is correct"

    username = get_username()
    if username:
        confirmation = input(f"Your username is {username}(y/n)? ").lower()
        if confirmation == "y":
            print(f"Welcome back {username}!")
        else:
            username = get_new_username()
            print(f"We will remember you {username}!")

    else:
        username = get_new_username()
        print(f"We will remember you {username}!")

def get_username():
    "Tries to get the username. If there is a file then returns the name, if doesn't returns None"

    filename = "username.json"

    try:
        with open(filename) as f_object:
            username = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    "It returns the name that is given by the user"
    filename = "username.json"

    print("Hello stranger!")
    username = input("What's your name? ")
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
    return username

greet_user()