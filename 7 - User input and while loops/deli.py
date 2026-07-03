sandwich_orders = [
    "tuna",
    "pastrami",
    "blt",
    "grilled cheese",
    "pastrami",
    "pastrami",
    ]

finished_sandwichs = []

while sandwich_orders:
    if "pastrami" in sandwich_orders:
        print("Deli run out of Pastrami sandwich")
        while "pastrami" in sandwich_orders:
            sandwich_orders.remove("pastrami")
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwichs.append(sandwich)

print("\nAll sandwichs done:")
for sandwich in finished_sandwichs:
    print(sandwich)