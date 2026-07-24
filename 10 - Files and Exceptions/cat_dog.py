cats_file = "cats.txt"
dogs_file = "dogs.txt"

try:
    with open(cats_file) as f_object:
        file = f_object.read()
        print(file)
except FileNotFoundError:
    print("File not found")

print("")

try:
    with open(dogs_file) as f_object:
        file = f_object.read()
        print(file)
except FileNotFoundError:
    print("File not found")