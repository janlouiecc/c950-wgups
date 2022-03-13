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

    # This function loads a hash table with the package data

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
