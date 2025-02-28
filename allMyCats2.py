catNames = []  # Create an empty list to store cat names

while True:  # Infinite loop to keep asking for cat names
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()  # Get user input for cat name

    if name == '':  # If the user enters nothing, break the loop
        break

    catNames = catNames + [name]  # Add the new cat name to the list (list concatenation)

print('The cat names are:')  # Print a header before displaying cat names

for name in catNames:  # Loop through each cat name in the list
    print(' ' + name)  # Print each cat name with a space before it for formatting
