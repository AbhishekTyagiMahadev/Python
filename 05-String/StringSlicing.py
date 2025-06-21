name = "Abcdefghijklmnopqrstuvwxyz"

print(len(name))
# string Slicing
print("\nstring Slicing")
print(name[0:5])
print(name[0:8:3]) 
print(name[0:-6])  # Or print(name[0:len(name)-6])
print(name[0:])  # Prints the whole string
print(name[:5])  # Same as name[0:5]