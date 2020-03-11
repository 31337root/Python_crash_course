rivers = {"nile": "egypt", }

for river in rivers:
    print("The " + river.title() + " runs through " +
        rivers[river].title())
for country in rivers.values():
    print("Value: " + country)
