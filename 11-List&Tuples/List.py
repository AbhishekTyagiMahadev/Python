list = [1, 2, 3, 4, 5, 6.36, "Abhisek", True]
print(type(list[0]))
print(type(list[1]))
print(type(list[2]))
print(type(list[3]))
print(type(list[4]))
print(type(list[5]))
print(type(list[6]))
print(type(list[7]))
print(type(list))
print(f"List = {list}")

if 6.36 in list:
    print("yes")
else:
    print("no")

    
list2 = [i for i in range(10)]
print(list2)
list2 = [i for i in range(10) if(i%2==0)]
print(list2)
