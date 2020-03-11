def describe_city(city, country = "no country specified."):
    """Display the city and country information."""
    print(city.title() + " is in " + country.title())

describe_city("Boston")
describe_city("Bogotá", "Colombia")
describe_city("Madrid", "España")
