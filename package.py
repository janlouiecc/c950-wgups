import csv


# Loads the data from the package csv file
def load_package_data(file_name, table):
    with open(file_name) as package_data:
        # reads through each line and separates data based on commas
        # each data is used to add as a parameter to instantiate a package object
        # package is then inserted into the hash table created using the package id as a key
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
        # reads through each line and separates data based on commas
        distance_data = csv.reader(distance_data, delimiter=',')
        for data in distance_data:
            table.append(data)

    # This loops through the distance data that is empty and finds the corresponding number in the list
    for i in range(len(table)):
        for j in range(len(table) + 3):
            if table[i][j] == '':
                table[i][j] = table[j - 3][i + 3]

    return table


# This function converts a floating point to time for output purposes
# A float is used to increment time based on the trucks speed
def convert_float_to_time(time):
    return '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))


# This function converts time back to a float for incrementing
# Time can then be converted back using the function above for output
def convert_time_to_float(time):
    float_time = time.split(':')
    return float(float_time[0]) + (float(float_time[1]) / 60)


class Package:

    # This instantiates a package object with the associated data provided
    # Also sets a delivery time to 0.0 meaning it has not yet been delivered
    def __init__(self, package_id, address, city, state, zip_code, deadline, mass_in_kg, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass_in_kg = mass_in_kg
        self.notes = notes
        self.delivery_time = 0.0

    # Reformat the print method for the object
    def __str__(self):
        return "Package #%s, %s, %s, %s, %s, %s, %skg, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                                  self.zip_code, self.deadline, self.mass_in_kg,
                                                                  self.notes, self.delivery_time)
