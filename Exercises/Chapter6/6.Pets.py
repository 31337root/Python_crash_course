tricci = {"kind": "Beagle", "owner": "Omar"} 
chiquita = {"kind": "Beagle", "owner": "Juliette"}

pets = [tricci, chiquita]

for pet in pets:
    for key, value in pet.items():
        print(key + ": " + str(value))
