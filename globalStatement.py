def spam():
    global eggs  # Declares 'eggs' as a global variable
    eggs = 'spam'  # Assigns 'spam' to the global variable 'eggs'

eggs = 'global'  # Initially assigns 'global' to the variable 'eggs'
spam()  # Calls the function, modifying the global 'eggs' to 'spam'
print(eggs)  # Prints 'spam' because 'eggs' was changed globally inside spam()
