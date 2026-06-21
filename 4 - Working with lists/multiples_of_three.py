multiples_of_three =  [value for value in range(3, 31, 3)]

for number in multiples_of_three:
    print(number)

print("The first three items in the list are:")
for number in multiples_of_three[:3]:
    print(number)

print("\nThree items from the middle of the list are:")
for number in multiples_of_three[3:6]:
    print(number)

print("\nThe last three items in the list are:")
for number in multiples_of_three[-3:]:
    print(number)