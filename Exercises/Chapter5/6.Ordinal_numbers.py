numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if numbers:
    for number in numbers:
        if number is 1:
            print("1st")
        elif number is 2:
            print("2nd")
        elif number is 3:
            print("3rd")
        else:
            print(str(number) + "th")
