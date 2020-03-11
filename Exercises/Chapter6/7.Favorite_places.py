favorite_places = {"Lola": ["Madrid", "Dublin", "Francia"],
    "Omar": ["Madrid", "Bogotá", "EEUU"],
    "Juliette": ["EEUU", "Madrid", "Bogotá"],
    }

for name, places in favorite_places.items():
    print("The favorites places of " + name + " are:")
    for place in places:
        print("\t- " + place)
