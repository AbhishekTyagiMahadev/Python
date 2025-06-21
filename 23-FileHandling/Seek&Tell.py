with open("Abhishek2.txt", "r") as f:
    print(type(f))
    print(f"We are at: {f.tell()}th byte")
    f.seek(20)
    print(f"We are at: {f.tell()}th byte")
    print(f.read(20))
    print(f"We are at: {f.tell()}th byte")
    f.seek(5)
    print(f"We are at: {f.tell()}th byte")
    print(f.read(20))
    print(f"We are at: {f.tell()}th byte")

with open("Abhishek3.txt", "a") as f:
    f.truncate(30)