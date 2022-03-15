from hash import ChainingHashTable
from package import *


class Main:
    # Creates a hash table for the packages
    packages_table = ChainingHashTable()

    # Loads the packages into the packages table
    load_package_data('packages.csv', packages_table)

    # Creates a list to store distances
    # Calls the function to load the data
    distance_data_list = load_distance_data('distances.csv')

    # Creates a list to store the addresses
    # Calls the function to load the addresses
    address_data_list = load_address_data('addresses.csv')

    # Creates three trucks to carry the packages
    truck1 = []
    truck2 = []
    truck3 = []

    load_truck_packages(truck1, truck2, truck3, packages_table)

    print(len(truck1))
    print(len(truck2))
    print(len(truck3), "\n")

    for _ in truck3:
        print(_, "\n")
