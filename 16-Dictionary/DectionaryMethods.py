empl1 = {
    1: 45, 
    2: 56,
    3: 70
}
empl2 = {
    5: 88, 
    6: 55
}

print(f"empl1: {empl1}")
empl1.update(empl2)

print(f"Updated empl1:{empl1}")
print(f"empl2: {empl2}")

empl2.clear()
print(f"empl2 cleared: {empl2}")

print(f"Remove Last pair: {empl1.popitem()}")
empl1.pop(5)
print(f"empl1 after pop(5): {empl1}")

del empl1  #use to delete Dectionary
