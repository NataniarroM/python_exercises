pizzas = ["Pepperoni", "Margherita", "Four-cheese"]

"""
for pizza in pizzas:
    print("I like " + pizza + " pizza")

print("I really love pizza")

"""

friends_pizzas = pizzas[:]

pizzas.append("Neapolitan")
friends_pizzas.append("Hawaiian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
