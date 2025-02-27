#The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string.
name = 'Pluto a cat'
newName = name[0:6] + 'the' + name[7:12]
print(newName)