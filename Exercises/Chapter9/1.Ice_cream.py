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


    def describe_restaurant(self):
        """Print the name an cuisine type"""
        print("Restaurant: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)


    def open_restaurant(self):
        """Print that the restaurant is open."""
        print("The restaurant " + self.restaurant_name + " is open.")


class IceScreamStand(Restaurant):

    """
    Model a specific ice cream restaurant.
    """
    def __init__(self, restaurant_name, cuisine_type):

        """Initialize the class."""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Arequipe", "Vanilla"]


    def display_flavors(self):
        """Display flavors"""
        print(self.flavors)


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

ice = IceScreamStand("Lolas", "Lola")
ice.display_flavors()
