import unittest
from city_country import city_formated

class CityCountryTest(unittest.TestCase):
    """Test for 11.city_country.py"""

    def test_city_country(self):
        "Do Santiago, Chile"
        formatted_name = city_formated("Santiago", "Chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

    def test_population(self):
        "Do Santiago, Chile - population 5000000"
        formatted_name = city_formated("Santiago", "Chile", "5000000")
        self.assertEqual(formatted_name, "Santiago, Chile - population 5000000")

unittest.main()
