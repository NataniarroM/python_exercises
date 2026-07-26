import unittest

from city_functions import formatted_city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        city = formatted_city_country("Bezerros", "Brazil")
        self.assertEqual(city, "Bezerros, Brazil")
    
    def test_city_country_population(self):
        city = formatted_city_country("Bezerros", "Brazil", "60000")
        self.assertEqual(city, "Bezerros, Brazil - 60000")

unittest.main()