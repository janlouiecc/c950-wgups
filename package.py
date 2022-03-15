import csv


# Loads the data from the package Excel file
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
def distance_between(address1, address2,
                     address_list, distance_list):
    i = 0
    # Finds the index for the target location of Address 2 from Address 1
    for _ in address_list:
        if address2 == address_list[i][1]:
            break
        else:
            i += 1
            continue

    # Finds the distance between Address 1 and Address 2 after the index has been found for Address 2
    j = 0
    for _ in address_list:
        if address1 == address_list[j][1]:
            return distance_list[j][i + 3]
        else:
            j += 1
            continue


# This function will load the trucks with packages along with their associated constraints
def load_truck_packages(truck1, truck2, truck3, packages):
    for i in range(1, 41):
        if packages.search(i).lookup("notes") == "Must be delivered with 15, 19" or \
                packages.search(i).lookup("notes") == "Must be delivered with 13, 19" or \
                packages.search(i).lookup("notes") == "Must be delivered with 13, 15" or \
                packages.search(i).lookup("package_id") == 13 or packages.search(i).lookup("package_id") == 15 or \
                packages.search(i).lookup("package_id") == 19:
            truck1.append(packages.search(i))
        elif packages.search(i).lookup("deadline") == "EOD" and packages.search(i).lookup("notes") is None:
            if len(truck2) > 10:
                truck3.append(packages.search(i))
            else:
                truck2.append(packages.search(i))
        elif packages.search(i).lookup("deadline") != "EOD" and packages.search(i).lookup("notes") is None:
            truck1.append(packages.search(i))
        elif packages.search(i).lookup("notes") == "Can only be on truck 2":
            truck2.append(packages.search(i))
        elif packages.search(i).lookup("mass") > 80.0 and packages.search(i).lookup("notes") is None:
            truck3.append(packages.search(i))
        else:
            truck3.append(packages.search(i))


class Package:

    def __init__(self, package_id, address, city, state, zip_code, deadline, mass_in_kg, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass_in_kg = mass_in_kg
        self.notes = notes

    def __str__(self):
        return "Package ID: %s\nAddress: %s, %s, %s %s\nDelivery Deadline: %s\nWeight in Kilos: %s kg\nSpecial " \
               "Notes: %s" % (self.package_id, self.address, self.city, self.state, self.zip_code, self.deadline,
                              self.mass_in_kg, self.notes)

    def lookup(self, descript):
        match descript:
            case "package_id":
                return self.package_id
            case "address":
                return self.address
            case "city":
                return self.city
            case "state":
                return self.state
            case "zip_code":
                return self.zip_code
            case "deadline":
                return self.deadline
            case "mass":
                return self.mass_in_kg
            case "notes":
                return self.notes
            case _:
                return "ERROR: data not found"
