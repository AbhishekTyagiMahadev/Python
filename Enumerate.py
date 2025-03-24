marks = [12, 45, 13, 77, 89, 10, 8]

indx = 0
for mark in marks:
    print(mark)
    if(indx == 3):
        print("index 3 founded")
    indx += 1


for indx, mark in enumerate(marks):
    print(mark)
    if(indx == 3):
        print("index 3 founded")
    indx += 1
    print("index = ",indx)