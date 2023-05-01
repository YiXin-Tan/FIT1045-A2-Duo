"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Itinerary.

@file itinerary.py
"""
import math
from city import City, create_example_cities, get_cities_by_name
import copy

class Itinerary():
    """
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        self.cities = [city for city in cities]

    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        distance_sum = 0
        for city_idx in range(len(self.cities) - 1):
            city1 = self.cities[city_idx]
            city2 = self.cities[city_idx + 1]
            distance_sum += city1.distance(city2)
        return distance_sum

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        self.cities.append(city)

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """
        min_dist = None
        min_city_idx = 0  # initialise min_city_idx (assume min index occurs when city is inserted at index 0)
        for city_idx in range(len(self.cities) + 1):
            cloned_itinerary_list = self.cities[:]  # create a copy
            # print(self.cities is cloned_itinerary_list) >>> False
            # print(self.cities[0] is cloned_itinerary_list[0]) >>> True
            cloned_itinerary_list.insert(city_idx, city)  # place city in cloned list
            dist = Itinerary(cloned_itinerary_list).total_distance() # creates a cloned instance, then get distance using it's instance method

            # TODO: ok to initialise like this?
            if not min_dist:
                min_dist = dist  # initialise min_dist (assume min distance occurs when city is inserted at index 0)
            elif dist < min_dist:
                min_dist = dist
                min_city_idx = city_idx

        self.cities.insert(min_city_idx, city)  # place city in actual list


    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"

        :return: a string representing the itinerary.
        """
        city_names = [city.name for city in self.cities]
        city_sequence = ' -> '.join(city_names)
        total_dist = round(self.total_distance())
        return f'{city_sequence} ({total_dist} km)'


if __name__ == "__main__":
    create_example_cities()
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],
                           get_cities_by_name("Kuala Lumpur")[0]])
    print(test_itin)

    # we try adding a city
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    # we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    # we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin)
