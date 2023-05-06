"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""
import os
from vehicles import Vehicle, create_example_vehicles, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from city import City
from country import Country, find_country_of_city
from csv_parsing import create_cities_countries_from_csv
from path_finding import find_shortest_path
from map_plotting import plot_itinerary

'''
Select a Vehicle from a list of existing vehicles (at least the three examples given in create_example_vehicles).

Select an origin and destination city from among all cities in worldcities_truncated.csv (any city must be selectable, including cities that have homonyms).

Find a shortest path between the two given cities, if there exists one.

If there is a path, create a map of the path, and exit. Otherwise, just exit.
'''
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
    :param valid_instances: A list of values to accept. Contains all vehicle, country or city .
    :return: validated instance within the given valid_instances list
    """
    if isinstance(valid_instances[0], City):
        # For ZQ,
        # if valid_instances are all city_instance, it will print out melbourne (1237), which is not pretty
        # valid_instances = [melb_obj,         kl_obj,    baoding_obj]
        # original __str__= [melbourne (1237), kl (4567), baoding (234544)]
        # thus we shorten it by getting city_instance.name
        # original.name   = [melbourne,        kl,        baoding]
        valid_names = [city.name for city in valid_instances]  # shorten __str__ of city instance
    else:
        valid_names = valid_instances  # retain __str__ of vehicle and country instance

    # allow users to only input whole numbers
    valid_user_options = [str(i) for i in range(0, len(valid_instances))]
    for i in range(0, len(valid_instances)):
        prompt += f'\n {i}. {valid_names[i]}'
    prompt += f'\nPlease enter a number [0-{len(valid_instances) - 1}]:'

    while True:
        try:
            user_option = input(prompt)
            assert user_option in valid_user_options, 'User option is not in valid inputs'
            clear_screen()
            return valid_instances[int(user_option)]  # return vehicle/city/country instance, terminates function and breaks from while loop
        except AssertionError:
            clear_screen()
            print('Invalid input, input must be an integer and within range, please try again')
            continue


def create_vehicles() -> [Vehicle]:
    """

    :return:
    """
    ccc = CrappyCrepeCar(200)
    ddd = DiplomacyDonutDinghy(100, 500)
    ttt = TeleportingTarteTrolley(3, 2000)
    return [ccc, ddd, ttt]

def select_vehicle(vehicles: [Vehicle]) -> Vehicle:
    vehicles_description = f'''
    CrappyCrepeCar can travel between any cities in the world at a {vehicles[0].speed} 
    DiplomacyDonutDinghy can travel between any two cities in the same country, or between international "primary" cities
    TeleportingTarteTrolley can travel between any two cities if the distance is less than a given maximum distance, in a fixed time.
'''

    #TODO: add vehicle description
    #TODO: print selected vehicle
    vehicle = validate_input('Select a delivery vehicle', vehicles)
    return vehicle


def validate_country(country_names: [str], origin_dest: str) -> [Country]:
    """
    NOT IN USE
    :param country_names:
    :param origin_dest:
    :return:
    """
    user_option = None
    filtered_country_names = []
    while True:  # while filtered_country_names != None
        try:
            user_option = input(f'Which country is the {origin_dest} city in?'
                                f'\nEnter the first character of the country [a-z]: ')
            user_option = user_option.upper()[0]
            for country_name in country_names:
                if user_option == country_name[0]:
                    filtered_country_names.append(country_name)

            assert filtered_country_names, 'No country found'  # filtered_country_names must != [], else no country is found

        except (AssertionError, IndexError):
            # handle AssertionError or IndexError
            print(f'Invalid input, please input again')
            continue  # continue to start of while loop and re-try

        break  # if theres no exception, break out of while loop

    clear_screen()
    validate_input(f"Here's countries starting with '{user_option}'\nPlease select country of the origin city'", filtered_country_names)


    # while not filtered_country_names:
    #     user_option = input('Enter the first character of your origin country [a-z] :').upper()[0]
    #     for country_name in country_names:
    #         if user_option == country_name[0]:
    #             filtered_country_names.append(country_name)
    # print(filtered_country_names)

def select_origin_and_destination_cities() -> (City, City):
    """
    Select origin city from a list of countries
    Select destination city from a list of countries
    :return: A list of the origin and destination city
    """
    create_cities_countries_from_csv("worldcities_truncated.csv")
    countries = list(Country.name_to_countries.values())

    origin_country = validate_input("Which country is the origin city in?", countries)
    origin_city = validate_input("Which is the origin city?", origin_country.cities)

    dest_country = validate_input("Which country is the destination city in?", countries)
    dest_city = origin_city
    while dest_city == origin_city:  # TODO: check same city
        dest_city = validate_input("which is the destination city?", dest_country.cities)

    # print(f'Origin city: {origin_city.name} {origin_country}')
    # print(f'Destination city: {dest_city.name} {dest_country}')

    return origin_city, dest_city


def display_vehicle_and_cities(vehicle: Vehicle, origin_city: City, dest_city: City) -> None:
    """

    :param vehicle:
    :param origin_city:
    :param dest_city:
    :return:
    """
    print(vehicle)
    print(f'Origin city: {origin_city.name} {find_country_of_city(origin_city)}')
    print(f'Destination city: {dest_city.name} {find_country_of_city(dest_city)}')

def main():
    """

    :return: None
    """
    print("===== Welcome to Papa Pierre's Pâtisseries =====")
    vehicles = create_vehicles()
    vehicle = select_vehicle(vehicles)
    origin_city, dest_city = select_origin_and_destination_cities()
    itinerary = find_shortest_path(vehicle=vehicle, from_city=origin_city, to_city=dest_city)
    display_vehicle_and_cities(vehicle, origin_city, dest_city)

    if itinerary:
        print(itinerary)
        plot_itinerary(itinerary=itinerary)
    else:
        print('No path found')

    # create_cities_countries_from_csv("worldcities_truncated.csv")
    # country_names = list(Country.name_to_countries.keys())
    # validate_country(country_names, 'origin')



if __name__ == '__main__':
    # TODO: add docstrings
    # TODO: implement clear_screen
    main()