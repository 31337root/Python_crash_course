topping = ""

while topping != "quit":
    topping = input("Give me a topping for your pizza\nOr write quit to exit: ")
    if topping != "quit":
        print("You add " + topping)
    else:
        print("Good bye.")
        break
