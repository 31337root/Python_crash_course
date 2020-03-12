from users import User

"""Admin and Privileges clases."""

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
