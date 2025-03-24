a = int(input("Enter the value = "))

if( a < 5 or a>10):
    raise ValueError("vlue should be between 5 and 10")

print(a)