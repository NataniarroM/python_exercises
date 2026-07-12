from datetime import date

class User():
    "Class used to represent users in general"

    def __init__(self, first_name, last_name, birthdate, e_mail, ):
        "Initialize attributes to describe a user"
        self.f_name = first_name
        self.l_name = last_name
        self.full_name = f"{self.f_name} {self.l_name}"
        self.birthdate = birthdate
        self.email = e_mail
        self.login_attempts = 0

    def describe_user(self):
        "Give a descripition neatly formatted of the user"
        print(f"{self.full_name}'s details:\nbirthdate: {self.birthdate}\ne-mail: {self.email}")
        
    def greet_user(self):
        "Print a formatted greeting to the user"
        print(f"Welcome {self.full_name}! Hope you are well")

    def increment_login_attempts(self):
        "Increments by one the number of login attempts"
        self.login_attempts += 1

    def reset_login_attempts(self):
        "Reset the number of login attempts to zero"
        self.login_attempts = 0

    def show_login_attempts(self):
        "Print the number of login attempts"
        print(f"Total of login attempts: {self.login_attempts}")

class Privileges():
    "A class that storages the possible privileges of a user"

    def __init__(self):
        self.privileges = ["Cand add post", "Cand delete post", "Can ban user"]

    def show_privileges(self):
        print(f"The user {self.full_name} has the privileges bellow: ")
        for privilege in self.privileges:
            print(f"-> {privilege}")

class Admin(User):
    "This class is used to represent administrator type users"

    def __init__(self, first_name, last_name, birthdate, e_mail):
        super().__init__(first_name, last_name, birthdate, e_mail)
        self.privileges = Privileges()

nicoli = Admin("Nicoli", "Da Silva", "21/07/2004", "nicoli@gmail.com")
nicoli.privileges.show_privileges()