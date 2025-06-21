def sum(n,m):
    """This is a sum function for addition"""       #This is a doc string
    print("n =",n, "\nm =",m)
    print("n + m =", n+m)

n = 10
m = 20
sum(n,m)
print(sum.__doc__)  #Accessing doc string