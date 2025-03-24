class Myclass:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod
  def add(a, b):
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
obj = Myclass(10)
print(obj.num)
obj.addtonum(6)
print(obj.num)

print(Myclass.add(5, 2))