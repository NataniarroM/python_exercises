filename = "guest.txt"

name = input("Digite seu nome: ")

with open(filename, "w") as file_object:
    file_object.write(name)