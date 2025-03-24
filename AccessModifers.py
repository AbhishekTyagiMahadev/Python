# There in no access modifiers in python
# Private

# class emp:
#     def __init__(self):
#         self.__name = "Abhishek"

# a = emp()
# # print(a.__name)   # can't accessable

# print(a._emp__name) # Accessable

# Protected
class emp:
    def __init__(self):
        self._name = "value"

class emp2(emp):
    def show(self):
        print(self._name)
    
a = emp()
b = emp2()
print(a._name) # Accessable   
b.show()