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
def clear_screen():
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
    # TODO: cant input same city
    valid_user_options = [str(i) for i in range(0, len(valid_inputs))]
    for i in range(0, len(valid_inputs)):
        prompt += f'\n {i}. {valid_inputs[i]}'
    prompt += f'\nPlease enter a number [0-{len(valid_inputs) - 1}]:'

    while True:
        try:
            user_option = input(prompt)
            assert user_option in valid_user_options, 'User option is not in valid inputs'
            clear_screen()
            return int(user_option)  # terminates function and breaks from while loop
        except AssertionError:
            clear_screen()
            print('Invalid input, input must be an integer and within range, please try again')
            continue

    # return int(user_option)


def select_vehicle() -> Vehicle:
    vehicle_instances = create_example_vehicles()
    #TODO: add vehicle description
    vehicle_idx = validate_input('Select a vehicle', vehicle_instances)
    return vehicle_instances[vehicle_idx]


def validate_country(country_names: [str], origin_dest: str) -> [Country]:
    az = ['a', ' b', ' c', ' d', ' e', ' f', ' g', ' h', ' i', ' j', ' k', ' l', ' m', ' n', ' o', ' p', ' q', ' r', ' s', ' t', ' u', ' v', ' w', ' x', ' y', ' z']
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


def validate_city(country: Country) -> City:
    pass


def validate_dest_city(origin_city_name: str, dest_city_names: [str]):

    dest_city_name = origin_city_name  # initialise

    while dest_city_name == origin_city_name:
        dest_city_idx = validate_input('Select the destination city', dest_city_names)
        dest_city_name = dest_city_names[dest_city_idx]

    return dest_city_idx

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
    # TODO: check same city
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

    # create_cities_countries_from_csv("worldcities_truncated.csv")
    # country_names = list(Country.name_to_countries.keys())
    # validate_country(country_names, 'origin')



if __name__ == '__main__':
    main()