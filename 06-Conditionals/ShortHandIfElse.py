a = 100
b = 15

# Basic shorthand if-else
print("A") if a > b else print("=") if (a == b) else print("B")

# Expanded: Take input from user and compare
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Shorthand if-else for user input
print(f"{x} > {y}") if x > y else print(f"{x} = {y}") if x == y else print(f"{y} > {x}")

# Expanded: Show difference as well
if x > y:
    print(f"{x} is greater than {y} by {x - y}")
elif x == y:
    print("Both numbers are equal.")
else:
    print(f"{y} is greater than {x} by {y - x}")