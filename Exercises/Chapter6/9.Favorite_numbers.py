favorite_numbers = {"Lola": [9, 2, 3],
    "Omar": [3, 2, 9], "Roberta": [5, 2, 3],
    "Pili": [2, 3, 4], "Juliette": [2, 3, 4],}

if favorite_numbers:
    print(favorite_numbers)
    for name, numbers in favorite_numbers.items():
        print("The favorites numbers of " + name + " are ", end="")
        for number in numbers:
            print(str(number), end=" ")
        print()
