cities = {
    "São Paulo":{"country":"brazil", "population":"11.904.961", "fact":"lots of people"},
    "Recife":{"country":"brazil", "population":"1.488.920", "fact":"great culture"},
    "Caruaru":{"country":"brazil", "population":"405.408", "fact":"good music"}
    }

for city, details in cities.items():
    print(f"City name: {city}")
    for detail, data in details.items():
        print(f"\t{detail}: {data}")
    print("\n")