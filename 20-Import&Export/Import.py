import math  # Import the built-in math module

number = float(input("Enter a number: "))

# Calculate square root
sqrt = math.sqrt(number)
print(f"The square root of {number} is {sqrt}")

# Calculate factorial (only for non-negative integers)
if number.is_integer() and number >= 0:
    factorial = math.factorial(int(number))
    print(f"The factorial of {int(number)} is {factorial}")
else:
    print("Factorial is only defined for non-negative integers.")

# Calculate sine of the number (in radians)
sine = math.sin(number)
print(f"The sine of {number} radians is {sine}")

# Calculate power (number raised to 2)
power = math.pow(number, 2)
print(f"{number} raised to the power 2 is {power}")

print(dir(math))