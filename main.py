from hash import ChainingHashTable
from package import *
from truck import *

# Creates a hash table for the packages
# Loads the packages into the packages table
packages = ChainingHashTable()
load_package_data('packages.csv', packages)

# Creates a list to store the addresses and their distances
# Calls the function to load the data
distance_data_list = load_distance_data('distances.csv')


# This function finds the distances between two addresses
def distance_between(address1, address2):
    i = j = 0

    for _ in distance_data_list:
        if address2 == distance_data_list[i][1]:
            break
        else:
            i += 1
            continue

    for _ in distance_data_list:
        if address1 == distance_data_list[j][1]:
            return float(distance_data_list[j][i + 3])
        else:
            j += 1
            continue


# Function to deliver the packages using the Nearest Neighbor Method
def deliver_the_packages(truck):
    last_known_address = hub = distance_data_list[0][1]
    # total_mileage = 0
    truck_load = len(truck.pkgs)

    while truck_load > 0:
        temp = []
        for _ in range(len(truck.pkgs)):
            temp.append(distance_between(last_known_address, truck.pkgs[_].lookup("address")))
        last_known_address = truck.pkgs[temp.index((min(temp)))].lookup("address")
        # total_mileage += min(temp)
        truck.deliver_pkg(temp.index((min(temp))))
        truck_load -= 1

    distance_between(last_known_address, hub)


class Main:
    # Creates three trucks to carry the packages
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()
    delayed_pkgs = []

    # Calls the load_truck_packages function to load the packages
    load_truck_packages(truck1.pkgs, truck2.pkgs, truck3.pkgs, delayed_pkgs, packages)

    deliver_the_packages(truck1)
    deliver_the_packages(truck2)
    deliver_the_packages(truck3)
    
    truck1.add_pkgs(delayed_pkgs[0])
    truck1.add_pkgs(delayed_pkgs[1])
    
    deliver_the_packages(truck1)
    