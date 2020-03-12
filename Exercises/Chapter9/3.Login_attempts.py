from users import User
from privileges import Privileges, Admin

user0 = User("Lola", "Moreno", 15, "F")
user1 = User("Omar", "Martínez", 21, "M")

user0.describe_user()
user0.greet_user()
user1.describe_user()
user1.greet_user()

print("\n\n--------------------")

user0.increment_login_attempts()
print(str(user0.login_attempts))
user0.reset_login_attempts()
print(str(user0.login_attempts))

admin = Admin("Lola", "Moreno", "15", "F")
admin.describe_user()
admin.privileges.show_privileges()
