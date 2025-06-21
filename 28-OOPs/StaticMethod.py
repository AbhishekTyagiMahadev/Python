class Math:
  def __init__(self, n, m):
    self.n = n
    self.m = m

  def sub(self):
    print(f"{self.n} - {self.m} = {self.n-self.m}")
    
  @staticmethod
  def add(a, b):
      return a + b

a = Math(5, 25)
a.sub()


print(Math.add(1, 2)) 
print(Math.add(7, 2))