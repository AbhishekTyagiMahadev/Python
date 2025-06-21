class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, {self.name}!")

obj = Person("Abhishek", 20)

# dir() - Lists all attributes and methods of the object
print("dir(obj):", dir(obj))

# __dict__ - Shows the object's attribute dictionary
print("obj.__dict__:", obj.__dict__)

# help() - Shows the help/documentation for the object/class
help(Person)