a = 4
b = 4
c = [1, 2, 3]
d = [1, 2, 3]
e = c

# Compare integers
print("a is b:", a is b)      # True, same memory location for small integers
print("a == b:", a == b)      # True, values are equal

# Compare lists
print("c is d:", c is d)      # False, different objects in memory
print("c == d:", c == d)      # True, values are equal

# Compare references
print("c is e:", c is e)      # True, both refer to the same object
print("c == e:", c == e)      # True, values are equal

# Show object ids
print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))
print("id(d):", id(d))
print("id(e):", id(e))