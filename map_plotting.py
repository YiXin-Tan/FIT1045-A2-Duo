"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It allows plotting an Itinerary as the picture of a map.

@file map_plotting.py
"""
from mpl_toolkits.basemap import Basemap #have to do 'pip install basemap'
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City


def plot_itinerary(itinerary: Itinerary, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2city3..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.
    """

    # Bounding box
    min_lat, max_lat, min_lon, max_lon = 5,5,5,5

    # Setting up the map
    m = Basemap(projection=projection, lat_0=0,lon_0=0,resolution="l",
                llcrnrlon=min_lon, llcrnrlat=min_lat, urcrnrlon=max_lon, urcrnrlat=max_lat)

    m.drawcoastlines(color='k', linewidth=0.5)
    m.fillcontinents(color='#c0c0c0')

    cities = itinerary.cities
    for i in range(len(cities) - 1):
        lat1, lon1 = cities[i].coordinates
        lat2, lon2 = cities[i+1].coordinates
        m.drawgreatcircle(lon1, lat1, lon2, lat2, linewidth=line_width, color=colour)

    filename = f"map{'_'.join(c.name for c in cities)}.png".replace(" ", "")
    plt.savefig(filename, dpi=200)
    print(f"Map saved to {filename}")
    plt.show()

if __name__ == "__main__":
    # create some cities
    city_list = list()

    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))

    # plot itinerary
    plot_itinerary(Itinerary(city_list))