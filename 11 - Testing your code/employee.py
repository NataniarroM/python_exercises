class Employee():
    "Simple class to represent an employee"

    def __init__(self, f_name, l_name, an_salary):
        self.first_name = f_name
        self.last_name = l_name
        self.annual_salary = an_salary

    def give_raise(self, value=5000):
        "It raises the atribbute salary with value given or with the default value"
        self.annual_salary += value