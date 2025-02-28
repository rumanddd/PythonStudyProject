eggs = ['cat', 'dog'] # This creates a new list.
print(id(eggs))
eggs.append('moose') # append() modifies the list "in place".
print(id(eggs)) # eggs still refers to the same list as before.
eggs = ['bat', 'rat', 'cow'] # This creates a new list, which has a new id
print(id(eggs)) # eggs now refers to a completely different list.