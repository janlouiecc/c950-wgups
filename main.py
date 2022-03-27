# Jan Louie Castro, Student ID# 003952787

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

    # This loops through the distances to find its destination address
    for _ in distance_data_list:
        if address2 == distance_data_list[i][1]:
            break
        else:
            i += 1
            continue

    # After the address has been found, the origin address is looped through
    # It finds its corresponding index for the address found above
    for _ in distance_data_list:
        if address1 == distance_data_list[j][1]:
            return float(distance_data_list[j][i + 3])
        else:
            j += 1
            continue


# Function to deliver the packages using the Nearest Neighbor Algorithm
def deliver_the_packages(truck, current_time):
    # This assigns the last known address initially to the hub
    last_known_address = hub = distance_data_list[0][1]

    # This assigns how many packages are initially in the truck
    # Total mileages is traced through the total_miles variable
    truck_load = len(truck.pkgs)
    total_miles = 0

    while truck_load > 0:
        temp = []  # Creates an empty list through each iteration

        # Loops through all packages still in the truck
        # Adds them into the empty list for comparison
        for _ in range(len(truck.pkgs)):
            temp.append(distance_between(last_known_address, truck.pkgs[_].address))

        last_known_address = truck.pkgs[temp.index((min(temp)))].address  # Updates the variable to the minimum value
        total_miles += min(temp)  # Calculates the total miles taken to get to the minimum value's address
        current_time += (min(temp) / 0.3) / 60  # Calculates its time at delivery, truck is going 18 mph
        print("Package #" + str(truck.pkgs[temp.index((min(temp)))].package_id) + " has been delivered to " +
              truck.pkgs[temp.index((min(temp)))].address + " at " + convert_float_to_time(current_time))
        truck.deliver_pkg(temp.index((min(temp))), current_time)  # Calls the deliver_package function
        truck_load -= 1  # decrements the truck load as the package has now been delivered

    print("The truck has now returned to the HUB")
    total_miles += distance_between(last_known_address, hub)  # Adds the mileage from final destination back to the hub
    current_time += (distance_between(last_known_address, hub) / 0.3) / 60  # Calculates the time at its arrival

    # Returns the total miles for the truck for this specific delivery
    # Returns the current time it has come back to the hub
    # Both items returned as a tuple
    return total_miles, current_time


class Main:
    print("Welcome to the WGUPS Package Tracking System!")  # The beginning of the program

    # The main menu starts with the option to deliver all packages
    while True:
        print("\nMAIN MENU")
        main_menu = input("1. Deliver Packages\n"
                          "2. Exit Program\n"
                          "SELECT - 1 or 2: ")
        if main_menu == str(1):
            # Creates three trucks to carry the packages
            # Saves packages that are delayed for a late delivery
            truck1 = Truck()
            truck2 = Truck()
            truck3 = Truck()
            delayed_with_deadline = []

            # Calls the load_truck_packages function to load the packages into the trucks
            load_truck_packages(truck1.pkgs, truck2.pkgs, truck3.pkgs, delayed_with_deadline, packages)

            # Creates the starting times for each truck
            # Floating point value is converted with the convert_float_to_time function
            truck1_time = 8.0
            truck2_time = 8.0
            truck3_time = 10.5

            # Calls the deliver_the_packages function for Truck 1
            print("\nTruck 1 is now delivering...")
            truck1_mileage, truck1_time = deliver_the_packages(truck1, truck1_time)
            Truck.total_mileage += truck1_mileage

            # Calls the deliver_the_packages function for Truck 1
            print("\nTruck 2 is now delivering...")
            truck2_mileage, truck2_time = deliver_the_packages(truck2, truck2_time)
            Truck.total_mileage += truck2_mileage

            # Loads the delayed packages into Truck 1
            print("\nTruck 1 is being being loaded for additional delivery...")
            for i in range(len(delayed_with_deadline)):
                truck1.add_pkgs(delayed_with_deadline[i])

            # Since truck 2 has returned and there are only two drivers
            print("Truck 2 driver has now logged on to Truck 3 for delivery...")

            print("\nTruck 1 is now delivering...")
            truck1_mileage, truck1_time = deliver_the_packages(truck1, truck1_time)

            # This gives the option to correct the address for package 9
            while True:
                address_update = input("\nAt 10:20, a correct address has been found for Package #" +
                                       str(packages.search(9).package_id) + ", would you like to update?"
                                                                            "\nY - Yes\nN - No\nSELECT - Y or N: ")

                if address_update.lower() == 'y':
                    packages.search(9).address = "410 S State St"
                    print("Package #" + str(packages.search(9).package_id), "'s address has been updated",
                          "to", str(packages.search(9).address) + ".\n")
                    break
                elif address_update.lower() == 'n':
                    print("Package #" + str(packages.search(9).package_id), "has not been updated.\n")
                    break
                else:
                    print("Invalid Entry\n")

            # Once package 9 has been updated, the truck is now set to deliver
            print("Truck 3 is now delivering...")
            truck3_mileage, truck3_time = deliver_the_packages(truck3, truck3_time)
            Truck.total_mileage += truck3_mileage

            print("\nTOTAL TIME TO DELIVER ALL PACKAGES: " + str(int(truck3_time - 8.0)) + " hours and " +
                  str(round(((truck3_time - 8.0) % 1) * 60)) + " minutes")
            print("TOTAL MILEAGE FOR ALL TRUCKS: " + "{:.1f}".format(Truck.total_mileage), "miles")
            break
        elif main_menu == str(2):
            # Exits the program
            exit()
        else:
            print("Invalid Entry")
            continue

    # After the packages have been delivered, a query option is available to utilize
    while True:
        print("\nWhat would you like to do next?")
        main_menu = input("1. Package Information Lookup (by delivery status at a point; inclusive)\n"
                          "2. Package Information Lookup (by delivery status between points; exclusive)\n"
                          "3. Exit Program\n"
                          "SELECT - 1, 2 or 3: ")
        if main_menu == str(1):  # This looks up the delivery status for each package at a certain point in time
            while True:
                package_lookup = input("\nPACKAGE STATUS AS OF __:__\nSELECT TIME (i.e. 08:00 to 17:00): ")
                if ':' not in package_lookup:
                    print("Invalid Entry")
                    continue
                else:
                    for i in range(40):
                        if packages.search(i + 1).delivery_time <= convert_time_to_float(package_lookup):
                            print("Package #" + str(packages.search(i + 1).package_id) + ", " + "Delivered on " +
                                  convert_float_to_time(packages.search(i + 1).delivery_time) + ", " +
                                  str(packages.search(i + 1).address) + ", " +
                                  str(packages.search(i + 1).city) + ", " +
                                  str(packages.search(i + 1).state) + ", " +
                                  str(packages.search(i + 1).zip_code) + ", " +
                                  str(packages.search(i + 1).mass_in_kg) + " kilograms")
                        else:
                            print("Package #" + str(packages.search(i + 1).package_id) + ", " + "Not Delivered" + ", " +
                                  str(packages.search(i + 1).address) + ", " +
                                  str(packages.search(i + 1).city) + ", " +
                                  str(packages.search(i + 1).state) + ", " +
                                  str(packages.search(i + 1).zip_code) + ", " +
                                  str(packages.search(i + 1).mass_in_kg) + " kilograms")
                    break
            continue
        elif main_menu == str(2):  # This looks up the delivery status of a package between two points in time
            while True:
                print("\nPACKAGE STATUS BETWEEN __:__ and __:__")
                package_lookup1 = input("SELECT TIME A (i.e. 08:00 to 17:00): ")
                package_lookup2 = input("SELECT TIME B (i.e. 08:00 to 17:00): ")
                if ':' not in package_lookup1 or ':' not in package_lookup2:
                    print("Invalid Entry")
                    continue
                else:
                    temp = []  # List is made for sorting the packages into the order of its delivered time
                    for i in range(40):
                        if convert_time_to_float(package_lookup1) <= packages.search(i + 1).delivery_time <= \
                                convert_time_to_float(package_lookup2):
                            temp.append(packages.search(i + 1))
                        else:
                            continue
                    temp.sort(key=lambda s: s.delivery_time)  # Packages are sorted by delivery time for printing
                    for _ in range(len(temp)):
                        print("Package #" + str(temp[_].package_id) + ", " +
                              "Delivered on " + convert_float_to_time(temp[_].delivery_time) + ", " +
                              str(temp[_].address) + ", " +
                              str(temp[_].city) + ", " +
                              str(temp[_].state) + ", " +
                              str(temp[_].zip_code) + ", " +
                              str(temp[_].mass_in_kg) + " kilograms")
                    break
            continue
        elif main_menu == str(3):
            # Exits the program
            exit()
        else:
            print("Invalid Entry")
            continue
