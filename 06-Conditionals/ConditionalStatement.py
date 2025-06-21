age = int(input("Enter your age="))
print("Your age is", age)
if(age<18):
    print("You can't drive")
else:
    print("you can drive")

num = 5
print(num==5)
print(num<5)

# elif condition
num2 = int(input("Enter your number +/- ="))
if(num2<0):
    print("Entered number is negative")
elif(num2>0):
    print("Entered number is positive")
else:
    print("Entered number is zero")