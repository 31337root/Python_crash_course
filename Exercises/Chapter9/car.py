class Car():
    """A simple attempt to repreent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self. year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()


    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles in it.")


    def update_odometer(self, mileage):
        if mileage >= slf.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        The initialize attributes specific to an electric car.
        """

        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    """A imple attempt to model a battery for an electic car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


    def upgrade_battery(self):
        """Ubgrade the battery."""
        if self.battery_size < 86:
            self.battery_size = 85
            print("Your new battery size is: " + str(self.battery_size))
        else:
            print("Your battery is big enough.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximattely " + str(range)
        message += " miles on a full charge."
        print(message)


my_tesla = ElectricCar("tesla", "model s", 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()