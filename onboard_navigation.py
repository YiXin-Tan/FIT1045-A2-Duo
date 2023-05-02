"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""
import os
from vehicles import Vehicle, create_example_vehicles
from city import City
from country import Country
from csv_parsing import create_cities_countries_from_csv
from path_finding import find_shortest_path
from map_plotting import plot_itinerary

'''
Select a Vehicle from a list of existing vehicles (at least the three examples given in create_example_vehicles).

Select an origin and destination city from among all cities in worldcities_truncated.csv (any city must be selectable, including cities that have homonyms).

Find a shortest path between the two given cities, if there exists one.

If there is a path, create a map of the path, and exit. Otherwise, just exit.
'''
def clear_screen():  # TODO: implement
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_input(prompt: str, valid_inputs: list) -> int:
    """

    :param prompt:
    :param valid_inputs:
    :return: validated index of the valid_input
    """
    # TODO: validate input, only allow int
    # TODO: cant input same city
    # TODO: use try/except

    for i in range(0, len(valid_inputs)):
        prompt += f'\n {i}. {valid_inputs[i]}'
    prompt += f'\nPlease enter a number [0-{len(valid_inputs)-1}]:'

    user_option = input(prompt)
    return int(user_option)


def select_vehicle() -> Vehicle:
    vehicle_instances = create_example_vehicles()
    #TODO: add vehicle description
    vehicle_idx = validate_input('Select a vehicle', vehicle_instances)
    return vehicle_instances[vehicle_idx]

def validate_country(countries: [Country]) -> [Country]:

    az = ['a', ' b', ' c', ' d', ' e', ' f', ' g', ' h', ' i', ' j', ' k', ' l', ' m', ' n', ' o', ' p', ' q', ' r', ' s', ' t', ' u', ' v', ' w', ' x', ' y', ' z']
    user_option = None
    while user_option not in az:
        # if not user_option:
        #     print('Invalid input, please try again.')
        user_option = input('Enter the first character of your origin country [a-z] :').lower()

    # for word in



def validate_city() -> City:
    pass


def select_origin_and_destination_cities() -> (City, City):
    """
    Select origin city from a list of countries
    Select destination city from a list of countries
    :return: A list of the origin and destination city
    """
    create_cities_countries_from_csv("worldcities_truncated.csv")
    country_instances = Country.name_to_countries
    country_names = list(Country.name_to_countries.keys())

    origin_country_idx = validate_input("Which country is the destination city in?", country_names)
    origin_country_name = country_names[origin_country_idx]
    origin_country_instance = Country.name_to_countries[origin_country_name]

    origin_city_instances = origin_country_instance.cities
    origin_city_names = [city.name for city in origin_city_instances]

    origin_city_idx = validate_input('Select the origin city', origin_city_names)
    origin_city_instance = origin_city_instances[origin_city_idx]
    print(origin_city_instance, origin_country_instance)

    dest_country_idx = validate_input('Which country is the destination city in?', country_names)
    dest_country_name = country_names[dest_country_idx]
    dest_country_instance = Country.name_to_countries[dest_country_name]
    dest_city_instances = dest_country_instance.cities
    dest_city_names = [city.name for city in dest_city_instances]
    dest_city_idx = validate_input('Select the destination city', dest_city_names)
    dest_city_instance = dest_city_instances[dest_city_idx]

    print(f'Origin city: {origin_city_instance.name} {origin_country_instance}')
    print(f'Destination city: {dest_city_instance.name} {dest_country_instance}')


    return origin_city_instance, dest_city_instance


def main():
    vehicle = select_vehicle()
    origin_city, dest_city = select_origin_and_destination_cities()
    itinerary = find_shortest_path(vehicle=vehicle, from_city=origin_city, to_city=dest_city)
    if itinerary:
        print(itinerary)
        plot_itinerary(itinerary=itinerary)
    else:
        print('No path found')



if __name__ == '__main__':
    main()