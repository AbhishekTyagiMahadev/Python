amount = int(input("Enter the amount = $"))
time = int(input("Enter the time in years = "))
rate = int(input("Enter the interest rate = "))
interest = (amount*time*rate)/100
total = interest + amount
print(f"interest =${interest}")
print(f"payble amount after {time} year is ${total}")