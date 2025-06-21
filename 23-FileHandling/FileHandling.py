f = open("Abhishek.txt", "r")

print(f)
text = f.read()
print(text)
f.close()


f = open("Abhishek2.txt", "w")
f.write("This is another file.\nI am writing data in this file in writing mode.")
f.close()

with open("Abhishek.txt", "a") as f:
    f.write("\nI am appending data in this file using \'with\' keyword.")