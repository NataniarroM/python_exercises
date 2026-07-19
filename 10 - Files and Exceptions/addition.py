def convert_to_int(number):
    "It tries to convert the argument to an integer, if don't it returns a message"

    try:
        number = int(number)
    except ValueError:
        print("Número inválido")
    else:
        return number

while True:
    f_number = convert_to_int(input("Digite o primeiro número: "))
    if f_number:
        break

print("\n")

while True:
    s_number = convert_to_int(input("Digite o segundo número: "))
    if s_number:
        break

sum = f_number + s_number
print(f"Resultado: {sum}")