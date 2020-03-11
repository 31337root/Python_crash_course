current_users = ["31337root", "Lola", "Lolamoreno", "Roberto", "admin"]
new_users = ["31337root", "Lola", "evefv", "4343", "123123"]

if current_users and new_users:
    for user in new_users:
        if user in current_users:
            print("You'll need to enter a diferent name.")
        elif user.lower() in current_users:
            print("You'll need to enter a diferent name.")
        elif user.upper() in current_users:
            print("You'll need to enter a diferent name.")
        else:
            print("The user is available.")
