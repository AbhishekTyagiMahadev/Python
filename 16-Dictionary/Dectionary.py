abhishek = {
    "name": "Abhishek",
    "age": 20,
    "city": "Meerut",
    "rollno": "1009"
}

print(abhishek["name"])
print(abhishek["age"])
print(abhishek["rollno"])
print(abhishek["city"]) #It print error if key is not exist in the dectionary
print(abhishek)
print(abhishek.get("name"))  #It print None if key is not exist in the dectionary
print(abhishek.keys())
print(abhishek.values())
print(abhishek.items())

for key in abhishek:
    print(f"{key} = {abhishek[key]}")
