class Myclass:
    def __init__(self, value):
        self.value = value
    def show(self):
        print(f"value is {self.value}")
    
    @property
    def ten_value(self):
        return 10*self.value
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value

    
obj = Myclass(20)
obj.show()
print(f"10*{obj.value} is {obj.ten_value}")
obj.ten_value = 50
obj.show()
print(f"10*{obj.value} is {obj.ten_value}")
