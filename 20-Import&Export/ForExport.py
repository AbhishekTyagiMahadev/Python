def hello():
    print("hello duniya")

def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

print("Current module name:", __name__)

if __name__ == "__main__":
    hello()
    greet("Abhishek")
    result = add(5, 7)
    print(f"Sum of 5 and 7 is: {result}")