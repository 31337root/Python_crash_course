import json

number = input("What's your favorite number: ")

with open("number.json", "w") as number_file:
    json.dump(number, number_file)
