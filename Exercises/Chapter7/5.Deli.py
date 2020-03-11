sandwich_orders = ["Chesse", "Salami", "Sausage", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []

print("We're out of pastrami, sorry.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("We'll prepare a " + sandwich + " sandwich!")
    finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
    print("We made a " + sandwich + " sandwich.")
