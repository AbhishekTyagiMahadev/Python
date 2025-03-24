set1 = {2, 4, 2, 6}
print(set1)

set2 = {"Tyagi", 4.25, 5, True}
print(set2)


# This is an empty set
set3 = set()
print(type(set3))

# Accessing the elements of a set
for value in set2:
    print(value)

# Set methods
s1 = {2, 4, 6, 8}
s2 = {2, 5, 6, 9}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)
print(s1.intersection(s2))
s3 = s1.symmetric_difference(s2)
print(s3)
s3 = s1.difference(s2)
print(s3)
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

# add()
# update()
# remove()
# pop()
# del
# clear()