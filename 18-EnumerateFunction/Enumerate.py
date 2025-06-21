marks = [12, 45, 13, 77, 89, 10, 8]

# Manual way to track index using a variable
indx = 0
for mark in marks:
    print(mark)
    if(indx == 3):
        print("index 3 founded")  # Print when index is 3
    indx += 1  # Increment index manually

# Using enumerate to get index and value together
for indx, mark in enumerate(marks):
    print(mark)
    if(indx == 3):
        print("index 3 founded")  # Print when index is 3
    print("index = ", indx)  # Print current index (after