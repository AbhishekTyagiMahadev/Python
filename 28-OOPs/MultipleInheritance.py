class Employee:
    def __init__(self, name, emp_id=None):
        self.name = name
        self.emp_id = emp_id

    def show(self):
        print(f"The name is {self.name}")
        if self.emp_id is not None:
            print(f"Employee ID: {self.emp_id}")

class Dancer:
    def __init__(self, dance, experience=0):
        self.dance = dance
        self.experience = experience

    def show(self):
        print(f"The dance is {self.dance}")
        print(f"Years of experience: {self.experience}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name, emp_id=None, experience=0):
        Employee.__init__(self, name, emp_id)
        Dancer.__init__(self, dance, experience)

    def show(self):
        print(f"Name: {self.name}")
        if self.emp_id is not None:
            print(f"Employee ID: {self.emp_id}")
        print(f"Dance style: {self.dance}")
        print(f"Years of experience: {self.experience}")

# Create an object with all details
o = DancerEmployee("Kathak", "Shivani", emp_id=101, experience=5)
print("Name:", o.name)
print("Dance:", o.dance)
print("Employee ID:", o.emp_id)
print("Experience:", o.experience)
o.show()

# Show method resolution order
print(DancerEmployee.mro())