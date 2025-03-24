class person:
    # name = 'Abhishkek Tyagi'
    # age = 20
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def info(self):
        print(f"{self.name} is {self.age} yesrs old")

a = person("Abhisek", 20)
b = person("Abhisek Tyagi", 21)
print(a.name)
print(a.age)
a.info()
print(b.name)
print(b.age)
b.info()