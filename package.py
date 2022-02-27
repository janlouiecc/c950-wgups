
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
        return "%s, %s, %s, %s, %s, %s, %s kg, %s" % (self.package_id, self.address, self.city, self.state,
                                                      self.zip_code, self.deadline, self.mass_in_kg, self.notes)
