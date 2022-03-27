
# This function will load the trucks with packages along with their associated constraints
def load_truck_packages(truck1, truck2, truck3, delayed, packages):
    # Since the trucks are being loaded manually, this function only loops through the given packages
    # A separate add_pkgs function is associated with the truck class for other purposes
    for i in range(40):
        # This statement groups the packages that have to be delivered together into one truck
        if packages.search(i + 1).notes == "Must be delivered with 15, 19" or \
                packages.search(i + 1).notes == "Must be delivered with 13, 19" or \
                packages.search(i + 1).notes == "Must be delivered with 13, 15" or \
                packages.search(i + 1).package_id == 13 or packages.search(i + 1).package_id == 15 or \
                packages.search(i + 1).package_id == 19:
            truck1.append(packages.search(i + 1))
        # Since these packages have no deadline and constraint, they either go into truck 2 or 3
        elif packages.search(i + 1).deadline == "EOD" and packages.search(i + 1).notes is None:
            if len(truck2) > 10:
                truck3.append(packages.search(i + 1))
            else:
                truck2.append(packages.search(i + 1))
        # The delayed packages are separated since they have a deadline
        # Truck 1 is set to deliver first and will add packages with a deadline to deliver ASAP
        elif packages.search(i + 1).deadline != "EOD":
            if packages.search(i + 1).notes == "Delayed on flight---will not arrive to depot until 9:05 am":
                delayed.append(packages.search(i + 1))
            else:
                truck1.append(packages.search(i + 1))
        # This groups packages that can only be on Truck 2
        elif packages.search(i + 1).notes == "Can only be on truck 2":
            truck2.append(packages.search(i + 1))
        else:
            truck3.append(packages.search(i + 1))


class Truck:
    total_mileage = 0

    # Truck objects can be instantiated with or without packages
    def __init__(self, pkgs=None):
        if pkgs is None:
            self.pkgs = []
        else:
            self.pkgs = pkgs

    # This function adds packages to the truck's list of packages
    def add_pkgs(self, pkg):
        self.pkgs.append(pkg)

    # This function delivers the package
    # It removes the package from the truck
    # It also sets the time of delivery for its associated package
    def deliver_pkg(self, index, time):
        self.pkgs[index].delivery_time = time
        self.pkgs.remove(self.pkgs[index])
