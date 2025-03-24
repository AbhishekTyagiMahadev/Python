# Reading a file
file = open('MyFile.txt','r')

print(file)
txt = file.read()
print(txt)
file.close()



# Writing a file
# file2 = open('MyFile2.txt','w')
file2 = open('MyFile2.txt','a')
file2.write("This is another file\n")
file2.close()

with open("MyFile2.txt", "a") as f:
    f.write("This is another with 'with'\n")


#another file methods
f = open("MyFile3.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    # m1 = line.split(",")[0]
    # m2 = line.split(",")[1]
    # m3 = line.split(",")[2]
    # print(f"maths={m1}")
    # print(f"science={m2}")
    # print(f"computer={m3}")
    m1 = line
    print(line)
    print(m1)

file = open('MyFile.txt','r')

file.seek(5)
print(file.tell())
data = file.read()
print(data)
print(file.tell())