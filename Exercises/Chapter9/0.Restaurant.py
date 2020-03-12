from restaurant import Restaurant

restaurant = Restaurant("Lola", "La vi")

print("Restaurant: " + restaurant.restaurant_name
    + "Cuisine type: " + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Omar", "Lols")
restaurant2 = Restaurant("Juliette", "Heidi")
restaurant3 = Restaurant("Chiquita", "Tricci")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
