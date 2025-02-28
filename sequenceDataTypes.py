name = 'Ulviyya'  # Assigning the string "Ulviyya" to the variable name

# Indexing using positive indexing (starts from 0)
print(name[0])  # Prints the first character: 'U'

# Indexing using negative indexing (starts from -1 at the last character)
print(name[-2])  # Prints the second-to-last character: 'y'

# Slicing using positive indexing (extracts characters from index 0 to 3)
print(name[0:4])  # Prints 'Ulvi'

# Slicing using implicit start (same as [0:4])
print(name[:4])  # Prints 'Ulvi'

# Slicing from index 2 to the end of the string
print(name[2:])  # Prints 'viyya'

# Membership test: checks if 'Ul' is a substring of name
print('Ul' in name)  # Prints True because 'Ul' is present in "Ulviyya"

# Iterating over the string and printing each character with decorations
for i in name:
    print('️❤❤❤ ' + i + ' ❤❤❤')  # Prints each letter surrounded by heart emojis
