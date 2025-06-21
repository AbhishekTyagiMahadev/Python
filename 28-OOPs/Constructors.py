class person:
    def __init__(self, n, a, rollno=None):
        self.name = n
        self.age = a
        self.rollno = rollno

    def info(self):
        if self.rollno is not None:
            print(f"{self.name} is {self.age} years old and has roll number {self.rollno}")
        else:
            print(f"{self.name} is {self.age} years old")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

    def update_rollno(self, new_rollno):
        self.rollno = new_rollno
        print(f"{self.name}'s new roll number is {self.rollno}")

# Create objects
a = person("Abhishek", 20)
b = person("Abhishek Tyagi", 21, 1009)

print(a.name)
print(a.age)
a.info()

print(b.name)
print(b.age)
b.info()

# Demonstrate birthday and roll number update
a.birthday()
a.update_rollno(1010)
a.info()

b.birthday()
b.update_rollno(2025)
b.info()