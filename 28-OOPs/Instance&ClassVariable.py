class Employee:
  companyName = "Apple" #class variable
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name  #instance variable
    self.raise_amount = 0.02
    Employee.noOfEmployees += 1
  def showDetails(self):
    print(f"Name: {self.name}")
    print(f"Company Name: {self.companyName}")
    print(f"Raise Amount: {self.raise_amount}")
    print(f"No of Employees: {self.noOfEmployees}\n")

emp1 = Employee("Abhishek")
emp1.raise_amount = 0.03
emp1.companyName = "Apple India" 
emp1.showDetails()

Employee.companyName = "Google"

emp2 = Employee("Vivek")
emp2.showDetails()

emp3 = Employee("Rohan")
emp3.companyName = "Nestle"
emp3.showDetails()