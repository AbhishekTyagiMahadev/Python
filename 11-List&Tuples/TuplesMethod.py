tup = (1, 2, 3, 4, 5 , 6 )
temp = list(tup)
temp.append(200)
print(temp)
temp.pop(3)
print(temp)
temp.pop(3)
print(temp)
tup = tuple(temp)
print(tup)

tup2 = (7, 8, 9)
tup3 = tup+tup2
print(tup3)

print(tup3.count(200))
print(tup3.count(6))

print(tup3.index(9))

print(f"len:{len(tup3)}")