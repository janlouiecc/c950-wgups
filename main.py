from hash import ChainingHashTable
from package import *
import csv


# This function loads a hash table with the package data
def load_package_data(file_name, table):
    with open(file_name) as package_data:
        package_data = csv.reader(package_data, delimiter=',')
        for package in package_data:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline = package[5]
            mass_in_kg = float(package[6])
            if package[7] == "":
                notes = None
            else:
                notes = package[7]

            pkg = Package(package_id, address, city, state, zip_code, deadline, mass_in_kg, notes)

            table.insert(package_id, pkg)


# This function loads the addresses and their distances into a distance data list
def load_distance_data(file_name, table):
    with open(file_name) as distance_data:
        distance_data = csv.reader(distance_data, delimiter=',')
        for data in distance_data:
            table.append(data)

    # This loops through the distance data that is empty and finds the corresponding number in the list
    for i in range(len(table)):
        for j in range(len(table) + 3):
            if table[i][j] == '':
                table[i][j] = table[j - 3][i + 3]


# This function loads the addresses into an address data list , delimiter=','
def load_address_data(file_name, table):
    with open(file_name) as address_data:
        address_data = csv.reader(address_data, delimiter=',')
        for data in address_data:
            table.append(data)


# This function finds the distances between two addresses
def distance_between(address1, address2):
    i = 0
    # Finds the index for the target location of Address 2 from Address 1
    for _ in address_data_list:
        if address2 == address_data_list[i][1]:
            break
        else:
            i += 1
            continue

    # Finds the distance between Address 1 and Address 2 after the index has been found for Address 2
    j = 0
    for _ in address_data_list:
        if address1 == address_data_list[j][1]:
            return distance_data_list[j][i + 3]
        else:
            j += 1
            continue


def minimum_distance_from(from_address):  # truck_packages
    i = 0
    j = 3
    for _ in distance_data_list:
        if distance_data_list[i][1] == from_address:
            min_dist = distance_data_list[i][j]
            for _ in range(len(distance_data_list[i])):

                if min_dist <= distance_data_list[i][j]:  # figure this out, how to keep  it in range
                    continue
                else:
                    min_dist = distance_data_list[i][j]
        i += 1


# Creates a hash table for the packages
packages_table = ChainingHashTable()

# Loads the packages into the packages hash table
load_package_data('packages.csv', packages_table)

# Creates a list to store distances between addresses
distance_data_list = []

# Loads the distance data into a list
load_distance_data('distances.csv', distance_data_list)

# Creates a list to store distances between addresses
address_data_list = []

# Loads the distance data into a list
load_address_data('addresses.csv', address_data_list)

truck1 = []
truck2 = []
truck3 = []

minimum_distance_from("195 W Oakland Ave")
