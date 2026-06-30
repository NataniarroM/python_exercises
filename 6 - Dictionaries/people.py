person_0 = {"first_name":"nicoli", "last_name":"da silva", "city":"duartina"}
person_1 = {"first_name":"francisco", "last_name":"da silva", "city":"bauru"}
person_2 = {"first_name":"nataniarro", "last_name":"da silva", "city":"bezerros"}

people = [person_0, person_1, person_2]

for person in people:
    print(f"{person["first_name"].title()} {person["last_name"].title()} from {person["city"].title()}")