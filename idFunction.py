eggs = ['cat', 'dog']  # This creates a new list with elements ['cat', 'dog']
print(id(eggs))  # Prints the memory address of the list "eggs"

eggs.append('moose')  # append() modifies the existing list by adding 'moose' at the end
print(id(eggs))  # The memory address remains the same because lists are mutable

eggs = ['bat', 'rat', 'cow']  # This creates a new list and assigns it to the variable "eggs"
print(id(eggs))  # Prints the new memory address, which is different from the previous one
