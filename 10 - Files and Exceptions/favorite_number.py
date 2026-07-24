import json

def get_fav_number():
    "It returns the number, if there is no file to get the number, it returns None"
    filename = "number.json"

    try:
        with open(filename) as f_object:
            number = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return number
    
def get_new_fav_number():
    "It stores the new number given by the user and then returns it"
    filename = "number.json"

    number = input("Digite seu número favorito: ")
    with open(filename, "w") as f_object:
        json.dump(number, f_object)
    return number

def tell_fav_number():
    "It shows different messages to either it knowing the number or discovering him"
    number = get_fav_number()
    if number:
        print(f"Your favorite number is {number}!")
    else:
        number = get_new_fav_number()
        print(f"Now I know your favorite number is {number}")

tell_fav_number()
        