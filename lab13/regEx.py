import re

# findall(): Returns all matches in a list
text = "The rain in Spain"
x = re.findall("ai", text)
print(x)  # ['ai', 'ai']

# search(): Returns the first match as a Match object
x = re.search("\s", text)
print("First whitespace found at position:", x.start())

# split(): Splits the string at each match
x = re.split("\s", text)
print(x)  # ['The', 'rain', 'in', 'Spain']

# sub(): Replaces matches with a specified string
x = re.sub("\s", "9", text)
print(x)  # 'The9rain9in9Spain'

# Using Metacharacters
pattern = r"\bS\w+"  # Word starting with 'S'
x = re.search(pattern, text)
print(x.group())  # 'Spain'

# Special Sequences and Sets
x = re.findall("[a-c]", text)  # Matches 'a', 'b', or 'c'
print(x)  # ['a', 'a', 'a']
