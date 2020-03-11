best_car = "Mercedes"

cars = ["Mercedes", "Nissan", "McLaren"]

print("Is " + cars[0] + " the best car?\nMy prediction is yes!")
print(cars[0] == best_car)
print("Is " + cars[1] + " the best car?\nMy prediction is nop :/")
print(cars[1] == best_car)
print("Is " + cars[2] + " the best car?\nMy prediction is nop :/")
print(cars[2] == best_car)
print(cars[0].lower() == best_car.lower())

if 1 > 0 and 0 < 1 and 3 == 3 or 3 != 3:
    print("LOLA")
print(best_car in cars)
print(best_car not in cars)
