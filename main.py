from hash import ChainingHashTable
from package import *
# from truck import *
import csv


# This function loads the addresses and their distances into a distance data list
def load_distance_data(file_name):
    table = []
    with open(file_name) as distance_data:
        distance_data = csv.reader(distance_data, delimiter=',')
        for data in distance_data:
            table.append(data)

    # This loops through the distance data that is empty and finds the corresponding number in the list
    for i in range(len(table)):
        for j in range(len(table) + 3):
            if table[i][j] == '':
                table[i][j] = table[j - 3][i + 3]

    return table


# This function loads the addresses into an address data list , delimiter=','
def load_address_data(file_name):
    table = []
    with open(file_name) as address_data:
        address_data = csv.reader(address_data, delimiter=',')
        for data in address_data:
            table.append(data)

    return table


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


# Creates a hash table for the packages
packages_table = ChainingHashTable()

# Loads the packages into the packages table
load_package_data('packages.csv', ChainingHashTable())

# Creates a list to store distances between addresses then calls the function to load the distance data into the list
distance_data_list = load_distance_data('distances.csv')

# Creates a list to store the addresses in the list then calls the function to load the addresses
address_data_list = load_address_data('addresses.csv')
