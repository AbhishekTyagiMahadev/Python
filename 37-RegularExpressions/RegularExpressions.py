import re

pattern = r"[A-Z]+ython"
text = '''Python is a versatile programming language known for its simplicity and readability. It is widely used in various fields such as web development, data science, automation, and artificial intelligence. With a large standard library and a supportive community, Python makes it easy for beginners to start coding and for professionals to build complex applications efficiently. Its cross-platform compatibility and extensive third-party packages further enhance its popularity among developers worldwide.
    '''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)   

for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])