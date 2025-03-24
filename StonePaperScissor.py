import random

com = random.randint(1, 3)
my = int(
    input("1 for Stone\n2 for Paper\n3 for Scissor \nEnter the number b/w 1 and 3 = ")
)
if 0 <= my > 3:
    print("Number is out of range")
    exit(0)

if com == 1:
    cinput = "Stone"
elif com == 2:
    cinput = "Paper"
else:
    cinput = "Scissor"


if my == 1:
    myinput = "Stone"
elif my == 2:
    myinput = "Paper"
else:
    myinput = "Scissor"


print(f"You select = {myinput}")
print(f"Computer select = {cinput}")


if (
    myinput == "Stone"
    and cinput == "Scissor"
    or myinput == "Paper"
    and cinput == "Stone"
    or myinput == "Scissor"
    and cinput == "Paper"
):
    print("You wins")
elif (
    cinput == "Stone"
    and myinput == "Scissor"
    or cinput == "Paper"
    and myinput == "Stone"
    or cinput == "Scissor"
    and myinput == "Paper"
):
    print("Computer Wins")
else:
    print("Draw")
