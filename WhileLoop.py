i = 1
while(i<=10):
    print(i)
    i += 1
else:
    print("Else executed")

num = 1
while(True):
    
    if(num==5 or num==7):
        print("skiped")
        num += 1
        continue
    print(num)
    num += 1
    if(num>10):
        print("breaked")
        break
