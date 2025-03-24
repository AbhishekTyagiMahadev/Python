List = [1, "Abhishek", True, 4.12]
print(type(List[0]))
print(type(List[1]))
print(type(List[2]))
print(type(List[3]))
print(type(List))
print(List)

if 4.12 in List:
    print("yes\n")
else:
    print("no\n")

# List Methods
list = [1,8,4,9,24]
print(list)
list.append(5)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print(list.index(9))
list.insert(5, 500)
print(list)
# list.extend(List)
list2 = list + List
print(list2)