#The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string.
name = 'Pluto a cat'  # A string containing the text "Pluto a cat"

# Creating a new string by slicing and modifying the original string
newName = name[0:6] + 'the' + name[7:12]
# name[0:6] -> 'Pluto ' (includes the space after 'Pluto')
# 'the' is inserted between
# name[7:12] -> ' cat' (starts from index 7 and includes the space before 'cat')

print(name)  # Prints the original string: "Pluto a cat"
print(newName)  # Prints the modified string: "Pluto the cat"
