filename = "naming_poll.txt"

while True:
    name = input("Por que você gosta de programaer?\nDiga(q para sair): ")

    if name == 'q':
        print("Saindo...")
        break

    with open(filename,"a") as file_object:
        file_object.write(f"{name}\n")


    print("\nGood reason! It was added to the list\n")