from time import sleep as dormir

filename = "guest_book.txt"

while True:
    name = input("Digite seu nome('q' para sair): ")

    if name == 'q':
        print("ending...")
        dormir(1.5)
        break

    with open(filename, "a") as file_object:
        file_object.write(f"{name}\n")

    print(f"Greetings {name}! Your name added to the data")