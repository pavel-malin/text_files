"""Displays data supplied about the city. (test_city.py)"""
def get_formatted_city(city, country, population=''):
    if population:
        city_country = city + ' ' + country + ' ' + population
    else:
        city_country = city + ' ' + country
    return city_country.title()