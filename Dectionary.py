abhishek = {
    "name": "Abhishek",
    "age": 20,
    "city": "Meerut",
    "rollno": "1009"
}

print(abhishek["name"])
print(abhishek["age"])
print(abhishek["rollno"])
print(abhishek["city"])
print(abhishek)
print(abhishek.get("name"))
print(abhishek.keys())
print(abhishek.values())


for key in abhishek:
    print(key,"=", abhishek[key])


# Dectionary methods
empl1 = {
    1:45, 2:56, 3:70
}
empl2 = {
    5:88, 6:55
}
print(empl1)
empl1.update(empl2)
print(empl1)
print(empl2)
empl2.clear()
print(empl2)
empl1.popitem()
empl1.pop(5)
print(empl1)




# del disc_name

