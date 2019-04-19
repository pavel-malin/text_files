import unittest
from city_funcions import get_formatted_city

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago Chile')

    def test_city_country_population(self):
        formatted_city = get_formatted_city('santiago', 'chile', '5000000')
        self.assertEqual(formatted_city, 'Santiago Chile 5000000')

unittest.main()