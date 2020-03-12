"""User class."""

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


