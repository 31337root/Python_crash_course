def make_car(manufacturer, model_name, **car_info):
    """Make a car directory with the car info."""

    car = {}
    car["manufacturer"] = manufacturer
    car["model_name"] = model_name

    for key, value in car_info.items():
        car[key] = value

    return car

print(make_car("subaru", "outback", color = "blue", tow_package = True))
