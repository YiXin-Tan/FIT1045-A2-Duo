"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Country.

@file country.py
"""
from tabulate import tabulate
from city import City, create_example_cities


class Country():
    """
    Represents a country.
    """
    name_to_countries = dict()  # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.
        #TODO: rename docstring parameters?
        :param country_name: The name of the country
        :param country_iso3: The unique 3-letter identifier of this country
	    :return: None
        """
        self.name = name
        self.iso3 = iso3
        self.cities = []

        Country.name_to_countries[self.name] = self  # populate this country instance into class variable name_to_countries

    def add_city(self, city: City) -> None:
        """
        Adds a city to the country.

        :param city: The city to add to this country
        :return: None
        """
        self.cities.append(city)  # populate this country's cities list with this city

    def get_cities(self, city_type: list[str] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument city_type can be given to specify a subset of
        the city types that must be returned.
        Cities that do not correspond to these city types are not returned.
        If None is given, all cities are returned.

        :param city_type: None, or a list of strings, each of which describes the type of city.
        :return: a list of cities in this country that have the specified city types.
        """
        if city_type:
            filtered_cities = []
            for city in self.cities:  # for each city in the specified country
                if city.city_type in city_type:  # check whether the city_type matches the filter criteria
                    filtered_cities.append(city)
            return filtered_cities
        else:
            return self.cities

    def print_cities(self) -> None:
        """
        Prints a table of the cities in the country, from most populous at the top
        to least populous. Use the tabulate module to print the table, with row headers:
        "Order", "Name", "Coordinates", "City type", "Population", "City ID".
        Order should start at 0 for the most populous city, and increase by 1 for each city.
        """
        table_headers = City.table_headers[:]  # clone from City class variable
        table_headers.insert(0, "Order")  # ["Order", "Name", "Coordinates", "City type", "Population", "City ID"]

        cities = [city.get_table_data() for city in self.cities]  # populate cities list with each city's data
        cities.sort(key=lambda city_list: int(city_list[3]), reverse=True)  # sorts population (in nested list) by descending order

        for i in range(len(cities)):
            cities[i].insert(0, i)  # insert order number at start of each nested list
        cities.insert(0, table_headers)  # insert table header at start of parent list

        print(f'Cities of {self.name}')
        print(tabulate(tabular_data=cities, numalign='left'))

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return self.name


def add_city_to_country(city: City, country_name: str, country_iso3: str) -> None:
    """
    Adds a City to a country.
    If the country does not exist, create it.

    :param city: The city to be added to this country
    :param country_name: The name of the country
    :param country_iso3: The unique 3-letter identifier of this country
    :return: None
    """
    if country_name not in Country.name_to_countries:
        # country doesn't exist yet
        country = Country(country_name, country_iso3)
    else:
        # country exists in class variable name_to_countries
        country = Country.name_to_countries[country_name]

    country.add_city(city)


def find_country_of_city(city: City) -> Country:
    """
    Returns the Country this city belongs to.
    We assume there is exactly one country containing this city.

    :param city: The city.
    :return: The country where the city is.
    """
    for country in Country.name_to_countries.values():
        if city in country.cities:
            return country


def create_example_countries() -> None:
    """
    Creates a few countries for testing purposes.
    Adds some cities to it.
    """
    create_example_cities()
    malaysia = Country("Malaysia", "MAS")
    kuala_lumpur = City.name_to_cities["Kuala Lumpur"][0]  # city object
    malaysia.add_city(kuala_lumpur)

    for city_name in ["Melbourne", "Canberra", "Sydney"]:
        add_city_to_country(City.name_to_cities[city_name][0], "Australia", "AUS")


def test_example_countries() -> None:
    """
    Assuming the correct countries have been created, runs a small test.
    """
    Country.name_to_countries["Australia"].print_cities()


if __name__ == "__main__":
    create_example_countries()
    test_example_countries()
