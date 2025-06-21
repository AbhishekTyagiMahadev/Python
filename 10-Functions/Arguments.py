# default arguments
def average(a=5, b=10):
    print("a=", a, "and b=", b)
    print("average is", (a+b)/2)
    return "Done"

c = average()
c = average(5, 6)
print(c)
 
# keyword arguments
c = average(b=15, a=25)
print(c)

def addition(*num):
    sum = 0
    for i in num:
        sum += i
    print(f"Sum of {num} is {sum}")
    print(type(num))

addition(1,2,3,4,5)