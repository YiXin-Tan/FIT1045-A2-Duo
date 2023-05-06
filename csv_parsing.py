"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country, add_city_to_country


def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    with open(path_to_csv, mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Getting csv header
            # csv headers: city,city_ascii,lat,lng,country,iso2,iso3,admin_name,capital,population,id
            city_ascii = row['city_ascii']
            lat = float(row['lat'])
            lng = float(row['lng'])
            city_type = row['capital']
            population = row['population']
            if population:
                population = int(population)  # population field is not empty
            else:
                population = 0  # population field is empty, treat population as 0
            city_id = int(row['id'])
            country_name = row['country']
            country_iso3 = row['iso3']

            # Format for creating and adding city
            new_city = City(name=city_ascii, coordinates=(lat, lng), city_type=city_type, population=population, city_id=city_id)
            add_city_to_country(city=new_city, country_name=country_name, country_iso3=country_iso3)


if __name__ == "__main__":
    # create_cities_countries_from_csv('worldcities_truncated_aus.csv')
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()