x = 4
print("This is global =",x)

def func():
    global x
    x = 5
    print("This is local =",x)

func()
print("x =", x)