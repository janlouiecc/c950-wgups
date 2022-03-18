
# This function will load the trucks with packages along with their associated constraints
def load_truck_packages(truck1, truck2, truck3, delayed, packages):
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
        elif packages.search(i).lookup("deadline") != "EOD":  # elif packages.search(i).lookup("deadline") != "EOD":  #
            if packages.search(i).lookup("notes") == "Delayed on flight---will not arrive to depot until 9:05 am":
                delayed.append(packages.search(i))
            else:
                truck1.append(packages.search(i))
        elif packages.search(i).lookup("notes") == "Can only be on truck 2":
            truck2.append(packages.search(i))
        elif packages.search(i).lookup("mass") > 80.0 and packages.search(i).lookup("notes") is None:
            truck3.append(packages.search(i))
        else:
            truck3.append(packages.search(i))


class Truck:

    def __init__(self, pkgs=None):
        if pkgs is None:
            self.pkgs = []
        else:
            self.pkgs = pkgs

    def add_pkgs(self, pkg):
        self.pkgs.append(pkg)

    def deliver_pkg(self, index):
        self.pkgs[index].delivery_time = 1
        self.pkgs.remove(self.pkgs[index])
