class emp:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"name = {self.name}")
        print(f"id = {self.id}")

class other(emp):
    def others(self):
        self.age = 20
        print(f"age = {self.age}")
    


a = emp("Abhishek Tyagi", 1009)
a.show()

b = other("Tyagi", 1005)
b.show()
b.others()
