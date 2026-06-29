rivers = {"são francisco":"brazil", "nile":"egypt", "rio prata":"argentine"}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\nThe list includes the rivers bellow: ")
for river in set(rivers.keys()):
    print(river.title())

print("\nThe list includes the countries bellow: ")
for country in set(rivers.values()):
    print(country.title())
