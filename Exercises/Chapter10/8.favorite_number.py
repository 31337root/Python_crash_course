import json

with open("number.json") as number_file:
    number = json.load(number_file)
    print("I know your favorite number! It's " + str(number))
