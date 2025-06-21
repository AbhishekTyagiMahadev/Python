class class1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(f"a = {self.a}\nb = {self.b}")

class class2(class1):
    def sum(self):
        print(f"sum = {self.a + self.b}")
    
obj = class2(int(input("Enter the value of a: ")), int(input("Enter the value of b: ")))
obj.show()
obj.sum()