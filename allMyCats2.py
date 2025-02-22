catNames = [] # Create an empty list
while True: # The main loop
   print('Enter the name of cat ' + str(len(catNames) + 1 ) + ' (Or enter nothing to stop.):')
   # Prompt for the cat name ^
   name = input() # Store the name
   if name == '': # If the name is empty
        break
   catNames = catNames + [name] # list concatenation
print('The cat names are:') # Print the string
for name in catNames: # Loop through the cat names
       print(' ' + name) # Print the cat name