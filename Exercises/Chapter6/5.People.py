lola = {"first name": "Lola", "last name": "Moreno", "age": 15,
    "city": "Madrid"}
omar = {"first name": "Omar", "last name": "Martinez", "age": 21,
    "city": "Bogotá"}
juliette = {"first name": "Juliette", "last name": "Martínez", "age": 23,
    "city": "Bogotá"}

people = [lola, omar, juliette]

for person in people:
    for key, value in person.items():
        print(key + ": " + str(value))
