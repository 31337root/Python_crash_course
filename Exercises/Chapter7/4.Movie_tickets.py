while True:
    age = int(input("Give me your age to give you the pay value: "))

    if age < 4:
        print("Your ticket is free.\nNEXT----->")
    elif age < 13:
        print("Your ticket cost $10\nNEXT----->")
    else:
        print("Your ticket cost $15\nNEXT----->")
