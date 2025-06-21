class Employee:
  def __init__(self, name, salary):
    self.name = name 
    self.salary = salary
    
  @classmethod
  def fromStr(cls, string):
    return cls(string.split("-")[0], int(string.split("-")[1]))
    
e1 = Employee("Abhishek Tyagi", 50000)
print(f"Name: {e1.name}")
print(f"Salary: {e1.salary}")

string = "John-12000"
e2 = Employee.fromStr(string)
print(f"Name: {e2.name}")
print(f"Salary: {e2.salary}")