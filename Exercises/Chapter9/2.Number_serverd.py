class Restaurant():

    """
    Model a restaurant by name and cuisine type
    describe_restaurant() - Print the name an cuisine type.
    open_restaurant() - Print that the restaurant is open.
    """
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing the instance.""" 
        self.restaurant_name =  restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Print the name an cuisine type"""
        print("Restaurant: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)


    def open_restaurant(self):
        """Print that the restaurant is open."""
        print("The restaurant " + self.restaurant_name + " is open.")


    def set_number_served(self, number):
        """Set a number to number_served"""
        self.number_served = number


    def increment_number_served(self, increment):
        """Increment the number of number_served"""
        self.number_served += increment


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

print("\n\n------------------------")
print(str(restaurant.number_served))
restaurant.number_served = 1014
print(str(restaurant.number_served))
restaurant.set_number_served(1015)
print(str(restaurant.number_served))
restaurant.increment_number_served(1013)
print(str(restaurant.number_served))
