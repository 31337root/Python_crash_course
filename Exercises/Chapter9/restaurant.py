"""Restaurant class"""

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
