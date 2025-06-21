def func():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print("Result:", result)
        return "Done"
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return "Error"
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return "Error"
    finally:
        print("Finally executed.")

print(func())