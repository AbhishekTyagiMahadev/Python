x = int(input("Enter the value of x="))

match x:
    case 0:
        print("X is 0")
    case 1:
        print("X is 1")
    case 2:
        print("X is 2")
    case 4:
        print("X is 4")
    case _:
        print("X is",x)