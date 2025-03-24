n = int(input("Enter the number of four digits = "))
list = []
sum = 0
num = n
while(n!=0):
    sum = int(n % 10)
    list.append(sum)
    n = int(n/10)


list.sort()
print(f"Largest digit in {num} is {list.pop()} and smallest digit is {list[0]}")

