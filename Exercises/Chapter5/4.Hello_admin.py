user_names = ["31337root", "Lola", "Lolamoreno", "Roberto", "admin"]

if user_names:
    for user in user_names:
        if user is not "admin":
            print("Hello " + user + ".")
        else:
            print("Hello admin, would you like to see a status report?")
else:
    print("We need to find some users!")


user_names = []

if user_names:
    for user in user_names:
        if user is not "admin":
            print("Hello " + user + ".")
        else:
            print("Hello admin, would you like to see a status report?")
else:
    print("We need to find some users!")
