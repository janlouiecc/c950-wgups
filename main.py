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


# This function loads the addresses into a distance data list
def load_distance_data(file_name, table):
    with open(file_name) as distance_data:
        distance_data = csv.reader(distance_data, delimiter=',')
        for data in distance_data:
            table.append(data)

    for i in range(len(table)):
        for j in range(len(table) + 2):
            if table[i][j] == '':
                table[i][j] = table[j-2][i+2]


# Creates a hash table for the packages
packages_table = ChainingHashTable()

# Loads the packages into the packages hash table
load_package_data('packages.csv', packages_table)

# Creates a list to store distances between addresses
distance_data_list = []

# Loads the distance data into a list
load_distance_data('distances.csv', distance_data_list)
