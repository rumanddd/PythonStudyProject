# Define a list of pet names
myPets = ['Rambo', 'Mia', 'Pluto']

# Ask the user to enter a pet name
print('Enter a pet name:')
name = input()  # Take input from the user

# Check if the entered name is in the list
if not name in myPets:
    print('I do not have any pet with the name ' + name)  # Print a message if the name is not found
else:
    print('Correct! ' + name + ' is one of my pets.')  # Print confirmation if the name exists in the list
