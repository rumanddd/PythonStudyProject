spam = [0, 1, 2, 3, 4, 5]  # Creates a list with elements [0, 1, 2, 3, 4, 5]
print(spam)  # Prints the original list

cheese = spam  # The reference (memory address) of spam is assigned to cheese, NOT a copy of the list
print(cheese)  # Prints cheese, which is the same list as spam

cheese[1] = 'Hello!'  # Modifies the second element in the list
print(spam)  # Since spam and cheese refer to the same list, spam is also affected

print(cheese)  # Prints cheese, which now contains the modified list
