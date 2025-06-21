letter = "My name is {} and I am from {}"
name = "Abhishek"
country = "India"
print(letter.format(name, country))

print(f"My name is {name} and I am from {country}")
print(f"My name is {{name}} and I am from {{country}}")

price = 49.23518
txt = f"price = {price:.3f}"
print(txt)
print(f"{2*24}")
print(type(f"{2*24}"))