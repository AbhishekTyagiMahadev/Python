a = input("Enter the number: ")

try:
    print(f"Table of {a} is:")
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("There is an error")
    print(e)

print("End of progrem")