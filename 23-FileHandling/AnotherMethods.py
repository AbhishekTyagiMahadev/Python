f = open("Abhishek.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f = open("Abhishek3.txt", "a")
lines = ["line1\n", "line2\n", "line3\n"]
f.writelines(lines)
f.close()