import csv
from hash import ChainingHashTable
from package import Package


# This function loads a hash table with the package data
def load_package_data(file_name):
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

            packages_table.insert(package_id, pkg)


packages_table = ChainingHashTable()
load_package_data('packages.csv')

# for i in range(40):
#     print(packages_table.search(i + 1), "\n")
