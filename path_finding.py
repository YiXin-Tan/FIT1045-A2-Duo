"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx

from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from csv_parsing import create_cities_countries_from_csv


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary:  # Itinerary | None
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """
    if isinstance(vehicle, CrappyCrepeCar):
        return Itinerary([from_city, to_city])  # most direct route given CCC, since it has a fixed travel speed
    else:
        g = networkx.Graph()
        cities_id = list(City.id_to_cities.keys())
        cities_len = len(cities_id)

        # for all cities, create individual nodes
        for city in cities_id:
            g.add_node(city)

        # attempt to create edges between all city nodes, goes through all combinations
        for i in range(cities_len - 1):
            city1 = get_city_by_id(cities_id[i])
            for j in range(i+1, cities_len):
                city2 = get_city_by_id(cities_id[j])
                travel_time = vehicle.compute_travel_time(city1, city2)
                if travel_time != math.inf:
                    # if a valid path is found, create an edge connecting these city's node
                    g.add_edge(city1.city_id, city2.city_id, weight=travel_time)

        try:
            # attempt to get shortest path
            path_sequence_ids = networkx.shortest_path(g, source=from_city.city_id, target=to_city.city_id)  # get shortest path yielding least time required
            path_sequence_obj = [get_city_by_id(city_id) for city_id in path_sequence_ids]  # populate with City instances
        except networkx.exception.NetworkXNoPath:
            # handle NetworkXNoPath error, as no path is found
            return  # terminate function
        else:
            # no NetworkXNoPath error
            return Itinerary(path_sequence_obj)


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")

    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))

    #we create some vehicles
    vehicles = create_example_vehicles()

    to_cities = set(from_cities)
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")

# References
# Math, Python Series 30 - Shortest route with networkx module 在网络许多路径中找 - YouTube
# https://www.youtube.com/watch?v=bu3I4EDBsKs
