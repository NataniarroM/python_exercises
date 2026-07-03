run = True

while run:
    age = input("Digite sua idade('quit' para sair): ").lower()
    
    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free")
    elif 3 <= age <= 12 :
        print("Your ticket costs $10")
    else:
        print("Your ticket costs $15")