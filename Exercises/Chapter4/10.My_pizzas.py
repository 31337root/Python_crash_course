#Program to print some useful information about pizza

pizzas = ["hawuaiana", "peperoni", "pollo"]

for pizza in pizzas:
    print("I like " + pizza)
print(pizzas[0] + " is nice\n" + pizzas[1] + " is interestign\n" + "Is tu " + pizzas[2])
print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append("mexicana")
friend_pizzas.append("ice cream")

for pizza in pizzas:
    print("good is " + pizza + " whit weed")
for pizza in friend_pizzas:
    print("good is " + pizza + " whit weed")
