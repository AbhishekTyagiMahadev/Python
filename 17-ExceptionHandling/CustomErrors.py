try:
    a = int(input("Enter the value = "))
    if a < 5 or a > 10:
        raise ValueError("Value should be between 5 and 10")
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("You entered a valid value:", a)
finally:
    print("Execution completed.")