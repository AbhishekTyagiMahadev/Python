name = "Abhishek"
print(name)
for i in name:
    print(i, end=",")
print("\n")

colors  = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i, end=(","))
    print("\n")

for i in range(10001):
    print(i,)

for i in range(51,101,10):
    print(i,)
else:
    print("Else executed")