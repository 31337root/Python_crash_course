import json

try:
    with open("number.json") as number_file:
        number = json.load(number_file)

except FileNotFoundError:
    number = input("What's your favorite number: ")

    with open("number.json", "w") as number_file:
        json.dump(number, number_file)
else:
    print("I know your favorite number! It's " + str(number))
