class person:
    name = "Abhishek"
    age = 20
    rollno = 1009
    def info(self):
        print(f"{self.name} is {self.age} year old")

a = person()
a.name = "Tyagi"
print(a.name, a.age ,a.rollno)
a.info()