"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""
import os
from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from city import City
from country import Country, find_country_of_city
from csv_parsing import create_cities_countries_from_csv
from path_finding import find_shortest_path
from map_plotting import plot_itinerary


# Global Constant
HEADER = "===== Papa Pierre's Pâtisseries ====="


def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_input(prompt: str, valid_instances: list):  # -> Vehicle|Country|City
    """
    Generates selection user interface.
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user
    :param valid_instances: A list of values to accept. Contains all vehicle, country or city
    :return: validated instance within the given valid_instances list
    """
    # shorten the displayed option label
    if isinstance(valid_instances[0], City):
        # default printing of City instance yields it name and id number e.g. "Melbourne (1036533631)"
        # by printing City instance.name, we can shorten it to "Melbourne"
        option_labels = [city.name for city in valid_instances]  # shorten __str__ of each city instance
    else:
        # default printing of Country is concise e.g. "Australia"
        # default printing of Vehicle is concise e.e. "CrappyCrepeCar (200 km/h)"
        # no need to modify
        option_labels = valid_instances  # retain __str__ of each vehicle or country instance

    # allow users to only input whole numbers
    valid_user_options = [str(i) for i in range(0, len(valid_instances))]
    for i in range(0, len(valid_instances)):
        prompt += f'\n {i}. {option_labels[i]}'  # create a number/label pair for each option
    prompt += f'\nPlease enter a number [0-{len(valid_instances) - 1}]:'

    print(HEADER)
    while True:
        try:
            user_option = input(prompt)
            assert user_option in valid_user_options, 'User option is not in valid inputs'
            clear_screen()
            return valid_instances[int(user_option)]  # return vehicle/city/country instance, terminates function and breaks from while loop
        except AssertionError:
            clear_screen()
            print('==========================================================================\n'
                  'Invalid input, input must be an integer and within range, please try again'
                  '\n==========================================================================')
            continue


def create_vehicles() -> [Vehicle]:
    """
    Creates 3 different vehicles, namely:
    - CrappyCrepeCar, with 200km/h speed
    - DiplomacyDonutDinghy, with 100km/h, with speed of 100km/h for intranational cities or 500km/h for international "primary" cities
    - TeleportingTarteTrolley, which travels a maximum range of 2000km in a fixed 3hr frame
    *Adapted from create_example_vehicles()

    :return: The list of vehicle instances
    """
    ccc = CrappyCrepeCar(200)
    ddd = DiplomacyDonutDinghy(100, 500)
    ttt = TeleportingTarteTrolley(3, 2000)
    return [ccc, ddd, ttt]


def select_vehicle(vehicles: [Vehicle]) -> Vehicle:
    """
    Select origin city from a list of countries
    Select destination city from a list of countries

    :param vehicles: The list of vehicle instances
    :return: The selected vehicle instance
    """
    vehicle = validate_input('Select a delivery vehicle', vehicles)
    return vehicle


def select_origin_and_destination_cities() -> (City, City):
    """
    Select origin city from a list of countries
    Select destination city from a list of countries

    :return: A pair of the origin and destination city instances
    """
    create_cities_countries_from_csv("worldcities_truncated.csv")
    countries = list(Country.name_to_countries.values())
    countries.sort(key=lambda x: x.name)  # sort countries (key is nested in the instance variable "name") by alphabetical order

    # select originating country, then origin city
    origin_country = validate_input('Which country is the ORIGIN city in?', countries)
    origin_city = validate_input('Which is the ORIGIN city?', origin_country.cities)

    # select destination country, then destination city
    dest_country = validate_input('Which country is the DESTINATION city in?', countries)
    dest_city = None  # initialise

    # while the destination city instance match that of the origin, or if the destination has yet exist
    while (dest_city == origin_city) or (dest_city == None):
        if dest_city:
            # there exist a previous input, which is invalid; asks for input again
            print('==========================================================================\n'
                  'Destination city matches the origin city, please input again\n'
                  '==========================================================================')
        dest_city = validate_input('Which is the DESTINATION city?', dest_country.cities)

    # print(f'Origin city: {origin_city.name} {origin_country}')
    # print(f'Destination city: {dest_city.name} {dest_country}')

    return origin_city, dest_city


def display_vehicle_and_cities(vehicle: Vehicle, origin_city: City, dest_city: City) -> None:
    """
    Prints a brief description of the vehicle, origin and destination cities

    :param vehicle: The delivery vehicle
    :param origin_city: The origin city
    :param dest_city: The destination city
    :return: None
    """
    print(HEADER)
    print(f'Delivery via {vehicle}')
    print(f'Origin: {origin_city.name}, {find_country_of_city(origin_city)}')
    print(f'Destination: {dest_city.name}, {find_country_of_city(dest_city)}')


def main():
    """
    Select a Vehicle from a list of existing vehicles.
    Select an origin and destination city from among all cities in worldcities_truncated.csv
    Find a shortest path between the two given cities, if there exists one.
    If there is a path, create a map of the path, and exit. Otherwise, just exit.

    :return: None
    """
    vehicles = create_vehicles()
    vehicle = select_vehicle(vehicles)
    origin_city, dest_city = select_origin_and_destination_cities()
    display_vehicle_and_cities(vehicle, origin_city, dest_city)
    print('Calculating shortest path...')
    itinerary = find_shortest_path(vehicle=vehicle, from_city=origin_city, to_city=dest_city)

    clear_screen()
    display_vehicle_and_cities(vehicle, origin_city, dest_city)
    if itinerary:
        # path is found via the given vehicle
        print(itinerary)
        plot_itinerary(itinerary=itinerary)
    else:
        # no path found via the given vehicle
        print('No path found')


if __name__ == '__main__':
    main()