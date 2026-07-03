dream_vacation = {}

while True:
    user_name = input("Digite o seu nome: ")
    destiny = input(f"{user_name}, if you could visit one place in the world, which one would it be? ")

    dream_vacation[user_name] = destiny

    choice = input("\nDo you want to enter another user(y/n)? ").lower()
    if choice == "n":
        break

print("\n==== Poll results ====")

for name, place in dream_vacation.items():
    print(f"{name} would like to go to {place}")