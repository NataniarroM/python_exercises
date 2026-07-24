from name_function import get_formatted_number

print("Enter 'q' at any time to quit")
while True:
    first = input("Please give me a first name: ").lower()
    if first == "q":
        break

    last = input("Please give me a last name: ").lower()
    if last == "q":
        break

    formatted_name = get_formatted_number(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")