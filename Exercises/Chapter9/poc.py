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
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def describe_user(self):
        """Print all the information about the user."""
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Sex: " + self.sex.title())


class Admin(User):

    """Set new attribute for admins."""

    def ___init___(self, first_name, last_name, age, sex):
        """Initialize the class"""
        super().__init__(self, first_name, last_name, age, sex)
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):

        """Print the privileges"""

        print(self.privileges)


admin = Admin("Lola", "Moreno", "15", "F")
admin.describe_user()
admin.show_privileges()
