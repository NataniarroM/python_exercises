def sandwich(*ingredients):
    print("\nThe sandwich has:\n")
    for ingredient in ingredients:
        print(ingredient)

sandwich("Bacon", "Lettuce", "Tomato", "Mayo")
sandwich("Cheddar", "Parmesan", "Brie", "Mustard")
sandwich("Sausage", "Chimichurri")