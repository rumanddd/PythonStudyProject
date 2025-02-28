import copy  # Importing the copy module to create copies of lists

spam = ['A', 'B', 'C', 'D']  # Creating a list with elements ['A', 'B', 'C', 'D']
id(spam)  # Retrieves the memory address of spam
print(id(spam))  # Prints the memory address of spam

cheese = copy.copy(spam)  # Creates a shallow copy of spam and assigns it to cheese
id(cheese)  # Retrieves the memory address of cheese
print(id(cheese))  # Prints the memory address of cheese, which should be different from spam

cheese[1] = 42  # Modifies the second element of cheese (changes 'B' to 42)
print(spam)  # Prints spam, which remains unchanged because cheese is a separate copy

print(cheese)  # Prints cheese, showing that the second element has been changed to 42
