class Demo:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Demo({self.value})"  # For print()

    def __repr__(self):
        return f"Demo({self.value})"  # For interpreter

    def __len__(self):
        return self.value  # For len()

    def __getitem__(self, index):
        return str(self.value)[index]  # For indexing

obj1 = Demo(20)
print(obj1)         # Calls __str__
print(len(obj1))    # Calls __len__
print(obj1[0])      # Calls __getitem__