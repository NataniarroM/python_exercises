class Restaurant():

    "Parent class that represents restaurants in general"

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        "Give a descripition of restaurant's atributes"
        print(f"The restaurant {self.name} is a {self.cuisine_type} type")

    def open_restaurant(self):
        "Print a message informing the restaurant is open"
        print(f"{self.name} is officially open")
    
    def set_number_served(self):
        "Set the number of clients served with the user's input"
        number = int(input("Digite o número de pessoas servidas: "))
        self.number_served = number

    def increment_number_served(self):
        "Increment the number of clients served with the user's input"
        number = int(input("Digite o número de pessoas servidas: "))
        self.number_served += number

    def show_number_served(self):
        "Show the number of clients served in a neatly format"
        print(f"The number of clients served is {self.number_served}")

class IceCreamStad(Restaurant):

    "Child class that inherits from Restaurant class and represents only Ice cream stands"

    def __init__(self, name, cuisine_type="Ice Cream Stand"):
        super().__init__(name, cuisine_type)
        self.flavors = ["Ice Blue", "Lime", "Cream", "Chocolate", "Mango"]

    def show_flavors(self):
        print("Flavors available:\n")
        for flavor in self.flavors:
            print(f"-> {flavor}")

    
oliver_ice_cream = IceCreamStad("Oliver's")
oliver_ice_cream.describe_restaurant()
oliver_ice_cream.show_flavors()