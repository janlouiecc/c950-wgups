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

    print(truck1)
    print(truck2)
    print(truck3)
    # print(truck1[0][1].lookup("address"))
    # print(truck2[0][1].lookup("address"))
    print(truck3[1].lookup("address"))
    print()

    # for _ in range(len(packages_table.table[0])):  # load up the truck manually using this small algo
    #     truck1.append(packages_table.table[0][_])
    #
    #     print(truck1[_][1].lookup("address"))
    # testt = packages_table.search(5)
    # print(testt.lookup("address"))
