list  = [10, 45, 9, 34, 12, 56, 12.90, 11]
print(list)

list.append(20)
print(list)

print(f"index of 12.90 is {list.index(12.90)}")

list.sort()
print(list)

list2 = list.copy()
list2.insert(5, 200)
print(list2)

list.extend(list2)
print(list)