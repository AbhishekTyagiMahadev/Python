class person:
    name = "Abhishek"
    age = 20
    rollno = 1009
    def info(self):
        print(f"{self.name} is {self.age} year old")

a = person()
print(f"name = {a.name}, age = {a.age} , rollno = {a.rollno}")
a.name = "Tyagi"
a.info()