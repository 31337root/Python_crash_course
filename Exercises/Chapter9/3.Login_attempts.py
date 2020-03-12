class User():
    """
    Modeling the user information
    describe_user() - Print all the information about the user.
    greet_user() - Print congrats to the user.
    """

    def __init__(self, first_name, last_name, age, sex):
        """Initializing the instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0
        self.privileges = Privileges()


    def describe_user(self):
        """Print all the information about the user."""
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Sex: " + self.sex.title())


    def greet_user(self):
        """Print congrats to the user"""
        print("Congrats " + self.first_name)


    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0"""
        self.login_attempts = 0


class Admin(User):

    """Set new attribute for admins."""

    def ___init___(self, first_name, last_name, age, sex):
        """Initialize the class"""
        super().__init__(self, first_name, last_name, age, sex)
        self.privileges = Privileges()


class Privileges():
    """Set provileges to admin users."""

    def __init__(self):
        """Initilize the instance."""

        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):

        """Print the privileges"""

        print(self.privileges)


#user0 = User("Lola", "Moreno", 15, "F")
#user1 = User("Omar", "Martínez", 21, "M")

#user0.describe_user()
#user0.greet_user()
#user1.describe_user()
#user1.greet_user()

#print("\n\n--------------------")

#user0.increment_login_attempts()
#print(str(user0.login_attempts))
#user0.reset_login_attempts()
#print(str(user0.login_attempts))

admin = Admin("Lola", "Moreno", "15", "F")
admin.describe_user()
admin.privileges.show_privileges()
