n1 = int(input("Enter te first number +ve = "))
n2 = int(input("Enter te second number +ve = "))
n3 = int(input("Enter te third number +ve = "))
n4 = int(input("Enter te fourth number +ve= "))


if(n1>=n2 and n1>=n3 and n1>=n4):
    print(f"{n1} is largest number")
elif(n2>=n1 and n2>=n3 and n2>=n4):
    print(f"{n2} is largest number")
elif(n3>=n1 and n3>=n2 and n4>=n4):
    print(f"{n3} is largest number")
elif(n4>=n1 and n4>=n2 and n4>=n3):
    print(f"{n4} is largest number")
else:
    print("numbers are equal")

# list  = []

# list.append(n1)
# list.append(n2)
# list.append(n3)
# list.append(n4)
# list.sort()
# print(f"largest number is {list.pop()}")