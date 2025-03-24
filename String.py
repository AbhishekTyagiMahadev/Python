name = "Abhishek"
print(name)
multiLine = """This is a
multi line string"""
print(multiLine)
print(name, multiLine)
# for character in multiLine:
#     print(character)


# string Slicing
print("\nstring Slicing")
print(name[0])
print(name[0:4])
print(name[0:-6])
# print(name[0:len(name)-6])
length = len(multiLine)
print(length,"\n")


# String methods
print("String methods")
x = "abhishek"
# Strings are immutable
print(len(x))
print(x.upper()) 
print(x.lower()) 
# print(x.rstrip("!"))
print(x.replace("abhishek", "tyagi"))
print(x.capitalize())
print(x.count("h"))
print(x.find("h"))