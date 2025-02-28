# Creating a list with four elements
spam = ["cat", "dog", "bat", "frog"]  # List of animal names
print(spam)  # Prints the entire list
print(spam[0])  # Prints the first element of the list

# Modifying an element in the list
spam[0] = "fly"  # Changing the first element from "cat" to "fly"
print(spam)  # Prints the updated list

# Creating a nested list (a list of lists)
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]  # First sublist has strings, second has numbers
print(spam[1])  # Prints the second sublist [10, 20, 30, 40, 50]
print(spam[1][0])  # Prints the first element of the second sublist (10)
print(spam[-2])  # Prints the first sublist ['cat', 'bat']
print(spam[1][1:4])  # Prints a slice of the second sublist [20, 30, 40]

# Getting the length of the list
print(len(spam))  # Prints the number of elements (2 sublists in this case)

# Adding a new item to the second sublist
spam[1] = spam[1] + ['new item']  # Appends 'new item' to the second sublist
print(spam)  # Prints the updated list

# Concatenating two lists
spam = [1, 2, 3] + ['A', 'B', 'C']  # Combines numbers and letters into one list
print(spam)  # Prints [1, 2, 3, 'A', 'B', 'C']

# Multiplying a list
spam = ['X', 'Y', 'Z'] * 3  # Repeats the list 3 times
print(spam)  # Prints ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

# Removing an element from the list
spam = ['cat', 'bat', 'rat', 'elephant']  # List of four elements
del spam[2]  # Removes the third element ('rat')
print(spam)  # Prints ['cat', 'bat', 'elephant']
