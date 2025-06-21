name = "Abhishek Tyagi"

# Convert to uppercase
print("Uppercase:", name.upper())

# Convert to lowercase
print("Lowercase:", name.lower())

# Convert to title case (first letter of each word capitalized)
print("Title case:", name.title())
print("Capitalize first letter:", name.capitalize())

# Replace a substring
print("Replace 'Tyagi' with 'Mahadev':", name.replace("Tyagi", "Mahadev"))

# Find the position of a substring
print("Position of 'shek':", name.find("shek"))  # Returns -1 if not found

# Check if string starts with a substring
print("Starts with 'Abh':", name.startswith("Abh"))

# Check if string ends with a substring
print("Ends with 'gi':", name.endswith("gi"))

# Count occurrences of a character
print("Count of 'a':", name.count("a"))

# Get the length of the string
print("Length:", len(name))

# Split the string into a list (by space)
print("Split by space:", name.split())

# Remove leading and trailing whitespace (not visible here, but for demonstration)
name_with_spaces = "   Abhishek Tyagi   "
print("Stripped:", name_with_spaces.strip())

# Check if all characters are alphabetic
print("Is alphabetic:", name.replace(" ", "").isalpha())

# Check if all characters are digits
print("Is digit:", name.isdigit())

# Center the string with padding
print("Centered (width 26):", name.center(26, '*'))