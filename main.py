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
def deliver_the_packages(truck, current_time):
    last_known_address = hub = distance_data_list[0][1]
    truck_load = len(truck.pkgs)
    total_miles = 0

    while truck_load > 0:
        temp = []
        for _ in range(len(truck.pkgs)):
            temp.append(distance_between(last_known_address, truck.pkgs[_].lookup("address")))
        last_known_address = truck.pkgs[temp.index((min(temp)))].lookup("address")
        total_miles += min(temp)
        current_time += (min(temp) / 0.3) / 60
        truck.deliver_pkg(temp.index((min(temp))), current_time)
        truck_load -= 1

    total_miles += distance_between(last_known_address, hub)
    current_time += (distance_between(last_known_address, hub) / 0.3) / 60

    return total_miles, current_time


class Main:
    print("Welcome to the WGUPS Package Tracking System!")

    # Creates three trucks to carry the packages
    # Saves packages that are delayed for a late delivery
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()
    delayed_with_deadline = []

    # Calls the load_truck_packages function to load the packages
    load_truck_packages(truck1.pkgs, truck2.pkgs, truck3.pkgs, delayed_with_deadline, packages)

    truck1_time = 8.0
    truck2_time = 8.0

    truck1_mileage, truck1_time = deliver_the_packages(truck1, truck1_time)
    Truck.total_mileage += truck1_mileage

    truck2_mileage, truck2_time = deliver_the_packages(truck2, truck2_time)
    Truck.total_mileage += truck2_mileage

    while True:
        address_update = input("There is a new address for Package #" +
                               str(packages.search(9).package_id) + ",would you like to update?\n"
                                                                    "1. Yes\n"
                                                                    "2. No\n"
                                                                    "Click 1 or 2: ")
        if address_update == str(1):
            packages.search(9).address = "410 S State St"
            print("\nPackage #" + str(packages.search(9).package_id), "'s address has updated",
                  "to", str(packages.search(9).address))
            break
        elif address_update == str(2):
            print("\nPackage #" + str(packages.search(9).package_id), "has not been updated.")
            break
        else:
            print("Invalid Entry\n")

    # Truck 2 driver delivers truck 3 after he gets back from delivering packages in truck 2
    truck3_time = truck2_time

    # Loads the delayed packages into Truck 1
    for i in range(len(delayed_with_deadline)):
        truck1.add_pkgs(delayed_with_deadline[i])

    truck1_mileage, truck1_time = deliver_the_packages(truck1, truck1_time)

    truck3_mileage, truck3_time = deliver_the_packages(truck3, truck3_time)
    Truck.total_mileage += truck3_mileage

    print("{:.1f}".format(Truck.total_mileage), "miles")
