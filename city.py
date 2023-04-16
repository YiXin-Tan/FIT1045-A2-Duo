"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class City.

@file city.py
"""
from __future__ import annotations #https://peps.python.org/pep-0563/
from typing import Tuple
import math
import geopy.distance

class City():
    """
    Represents a city.
    """

    #associates an id to an instance of City
    id_to_cities = dict()

    # associates city names to a list of instances of City.
    # We use a list because there may be multiple cities with the same name.
    name_to_cities = dict()

    table_headers = ["Name", "Coordinates", "City type", "Population", "City ID"]

    def __init__(self, name: str, coordinates: Tuple[float, float], city_type: str,\
                  population: int, city_id: int) -> None:
        """
        Initialises a city with the given data.

        :param name: the name of the city.
        :param coordinates: the coordinates of the city (latitute, longitude)
        :param city_type: the type of city (e.g. admin). Can be empty.
        :population: the population of the city.
        :city_id: an integer unique to this city.
        :return: None
        """
        self.name = name

        self.coordinates = coordinates

        self.city_type = city_type

        self.population = population

        self.city_id = city_id

        #TODO

    def distance(self, other_city: City) -> int:
        """
        Returns the distance in kilometers between two cities using the great circle method,
        rounded up to an integer.

        :param other_city: a city to measure the distance to
        :return: the rounded-up distance in kilometers
        """
        #TODO

    def __str__(self) -> str:
        """
        Returns the name of the city and city ID in parentheses.
        For example, "Melbourne (1036533631)"

        :return: a string representing the city.
        """
        #TODO

    def get_table_data(self) -> list[str]:
        """
        Returns a list of data about the city.
        It follows the list given by the class variable table_headers, so the attributes are
        self.name, self.coordinates, self.city_type, self.population, self.city_id,
        in this order. For example,
        ['Melbourne', "('-37.8136', '144.9631')", 'admin', '4529500', '1036533631'].

        :return: A list of data about the city.
        """
        #TODO


def get_city_by_id(city_id: int) -> City | None:
    """
    Given a city ID, returns the city with that ID if one is known, None otherwise.

    :param city_id: the ID of the city.
    :return: the city with that ID if one is known, None otherwise.
    """
    #TODO


def get_cities_by_name(city_name: str) -> list[City]:
    """
    Given the name, returns the list of cities known by this name. 
    If no city is known, returns an empty list.

    :param city_name: the name of the city.
    :return: the list of cities known by this name. 
    """
    #TODO



def create_example_cities() -> None:
    """
    Creates a few cities for testing purposes.
    """
    City("Melbourne", (-37.8136, 144.9631), "admin", 4529500, 1036533631)
    City("Canberra", (-35.2931, 149.1269), "primary", 381488, 1036142029)
    City("Sydney", (-33.865, 151.2094), "admin", 4840600, 1036074917)
    City("Kuala Lumpur", (3.1478, 101.6953), "primary", 8639000, 1458988644)
    #an example of two cities with the same name
    City("Santiago", (-33.45, -70.6667), "primary", 7026000, 1152554349)
    City("Santiago",	(19.45, -70.7), "admin", 1343423, 1214985348)
    #an example of a city without a specific city type
    City("Baoding", (38.8671, 115.4845), "", 11860000, 1156256829)


def test_example_cities() -> None:
    """
    Assuming the correct cities have been created, runs a small test.
    """
    melbourne = get_city_by_id(1036533631)
    sydney = get_cities_by_name("Sydney")[0]
    print(melbourne)
    print(f"Melbourne's name is {melbourne.name}")
    print(f"Melbourne's population is {melbourne.population}")
    print(f"The distance between Melbourne and Sydney is {melbourne.distance(sydney)} km")


if __name__ == "__main__":
    create_example_cities()
    test_example_cities()
