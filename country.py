"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Country.

@file country.py
"""
from tabulate import tabulate
from city import City, create_example_cities, get_cities_by_name

class Country():
    """
    Represents a country.
    """
    # {country_name: country_obj}
    name_to_countries = dict()  # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.

        :param country_name: The name of the country
        :param country_iso3: The unique 3-letter identifier of this country
	    :return: None
        """
        self.name = name
        self.iso3 = iso3
        self.cities = []  # [city_obj] TODO: self.cities => None? ensure that it is populated with the cities added to the country.
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
        filtered_cities = []
        if city_type:
            for check_city_type in city_type:  # for each filter criteria
                for city in self.cities:  # for each city in the specified country
                    # check whether the city_type matches the filter criteria
                    if city.city_type == check_city_type:
                        filtered_cities.append(city)
        else:
            for city in self.cities:
                filtered_cities.append(city)
        return filtered_cities


    def print_cities(self) -> None:
        """
        Prints a table of the cities in the country, from most populous at the top
        to least populous. Use the tabulate module to print the table, with row headers:
        "Order", "Name", "Coordinates", "City type", "Population", "City ID".
        Order should start at 0 for the most populous city, and increase by 1 for each city.
        """
        # test code
        print(self.cities)
        for city in self.cities:
            print(city.name)

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return self.name


def add_city_to_country(city: City, country_name: str, country_iso3: str) -> None:
    """
    Adds a City to a country.
    If the country does not exist, create it.

    :param country_name: The name of the country
    :param country_iso3: The unique 3-letter identifier of this country
    :return: None
    """
    if country_name in Country.name_to_countries:
        # country exists in class variable name_to_countries
        existing_country = Country.name_to_countries[country_name] # get existing country instance
        existing_country.add_city(city)
        # print(existing_country.cities)
    else:
        # country doesn't exist yet
        new_country = Country(country_name, country_iso3)
        new_country.add_city(city)


def find_country_of_city(city: City) -> Country:
    """
    Returns the Country this city belongs to.
    We assume there is exactly one country containing this city.

    :param city: The city.
    :return: The country where the city is.
    """
    for country_name, country_obj in Country.name_to_countries.items():
        if city in country_obj.cities:
            return country_obj

def create_example_countries() -> None:
    """
    Creates a few countries for testing purposes.
    Adds some cities to it.
    """
    create_example_cities()
    malaysia = Country("Malaysia", "MAS")
    kuala_lumpur = City.name_to_cities["Kuala Lumpur"][0]  # city object
    malaysia.add_city(kuala_lumpur)
    malaysia.print_cities()

    for city_name in ["Melbourne", "Canberra", "Sydney"]:
        add_city_to_country(City.name_to_cities[city_name][0], "Australia", "AUS")

def test_example_countries() -> None:
    """
    Assuming the correct countries have been created, runs a small test.
    """
    Country.name_to_countries["Australia"].print_cities()


if __name__ == "__main__":
    # create_example_countries()
    # test_example_countries()

    # # print(City.name_to_cities["Melbourne"][0])
    # # find_country_of_city(City.name_to_cities["Melbourne"])
    au = Country('Australia', 'AUS')
    nz = Country('New Zealand', 'NZL')
    mel = City("Melbourne", (-37.8136, 144.9631), "admin", 4529500, 1036533631)
    auck = City('Auckland', (1,3), 'admin', 30, 3)
    add_city_to_country(mel, 'Australia', 'AUS')
    add_city_to_country(auck, 'New Zealand', 'NZ')

    au.print_cities()
    nz.print_cities()
    # # print(au.cities)
    # # print(nz.cities)
    # print(find_country_of_city(auck))

