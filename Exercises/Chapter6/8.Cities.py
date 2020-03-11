cities = {"Madrid": {"Country": "Spain", "Population": 8, "Fact": "Love place"},
    "Bogotá": {"Country": "Colombia", "Population": 8, "Fact": "Happy place"},
    "New York": {"Country": "EEUU", "Population": 1, "Fact": "Crazy place"},
    }

for city, info in cities.items():
    print(city.title() + ":")
    for key, value in info.items():
        print("\t" +  key + ": " + str(value))
