letter = "My name is {} and i am from {}"
name = "Abhishek"
country = "India"
print(letter.format(name, country))
print(f"My name is {name} and i am from {country}")
print(f"My name is {{name}} and i am from {{country}}")

price = 49.23518
txt = f"price = {price:.3f}"
print(txt)
print(f"{2*24}")
print(type(f"{2*24}"))