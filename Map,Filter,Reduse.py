from functools import reduce
def cube(x):
    return x*x*x

# print(cube(2))


l = [1, 3, 5, 8, 4]
newl = []
for i in l:
    newl.append(cube(i))

# map
print(l,newl)
newl = list(map(cube, l))
print(newl)

# filter
def filter_fun(x):
    return x>=5

new2 = list(filter(filter_fun, l))
print(new2)


# reduce
def sum(x, y):
    return x + y

print(reduce(sum, l))