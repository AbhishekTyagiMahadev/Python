s1 = {2, 4, 6, 8}
s2 = {2, 5, 6, 9}

# union() - returns a new set with all elements from both sets
print("Union:", s1.union(s2))

# update() - adds elements from another set to the current set
s1.update(s2)
print("After update:", s1)

# intersection() - returns a new set with common elements
print("Intersection:", s1.intersection(s2))

# intersection_update() - updates the set with common elements
s1.intersection_update(s2)
print("After intersection_update:", s1)

# difference() - returns elements in the first set but not in the second
diff = s1.difference(s2)
print("Difference:", diff)

# difference_update() - removes elements found in another set
s1 = {2, 4, 6, 8}
s1.difference_update(s2)
print("After difference_update:", s1)

# symmetric_difference() - elements in either set, but not both
s3 = s1.symmetric_difference(s2)
print("Symmetric Difference:", s3)

# symmetric_difference_update() - updates set with symmetric difference
s1 = {2, 4, 6, 8}
s1.symmetric_difference_update(s2)
print("After symmetric_difference_update:", s1)

# isdisjoint() - checks if sets have no elements in common
print("Is disjoint:", s1.isdisjoint(s2))

# issubset() - checks if set is a subset of another
print("Is subset:", {2, 6}.issubset(s2))

# issuperset() - checks if set is a superset of another
print("Is superset:", s2.issuperset({2, 6}))

# add() - adds a single element
s1 = {1, 2, 3}
s1.add(4)
print("After add:", s1)

# remove() - removes an element (raises error if not found)
s1.remove(4)
print("After remove:", s1)

# discard() - removes an element (no error if not found)
s1.discard(10)
print("After discard:", s1)

# pop() - removes and returns an arbitrary element
elem = s1.pop()
print("After pop:", s1, "| Popped element:", elem)

# clear() - removes all elements
s1.clear()
print("After clear:", s1)

# copy() - returns a shallow copy of the set
s2_copy = s2.copy()
print("Copy of s2:", s2_copy)