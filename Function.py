def AddNum(a, b):
    sum = a + b
    print("sum  is =",sum)

def Compair(a, b):
    if(a>b):
        print(a,"is greater and",b,"is smaller")
    else:
        print(b,"is greater and",a,"is smaller")

def extraFunction():
    pass 


a = 10
b = 45
AddNum(a, b)
Compair(a, b)

# default arguments
def average(a=5, b=10):
    print("a=", a, "and b=", b)
    print("average is", (a+b)/2)
    return "Done"

c = average()
 
# keyword arguments
c = average(b=15)
print(c)

