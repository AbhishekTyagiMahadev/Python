class Myclass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"value is {self._value}")
    @property
    def ten_value(self):
        self._value = self._value*10
        return self._value
    
    @ten_value.setter
    def ten_value(self, newvalue):
        self._value = newvalue*10

    
obj = Myclass(4)
obj.show()
print(f"value is {obj.ten_value}")
obj.ten_value = 20
obj.show()
print(f"value is {obj.ten_value}")
