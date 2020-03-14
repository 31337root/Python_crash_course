while True:
    number1 = input("Give me a number: ")
    number2 = input("Give me another number: ")

    try:
        result = int(number1) + int(number2)
    except ValueError:
        print("Give just numbers.")
    else:
        print(str(result))
