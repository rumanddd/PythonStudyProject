def spam():
    global eggs  # Declares 'eggs' as a global variable
    eggs = 'spam'  # Assigns 'spam' to the global variable 'eggs'


def bacon():
    eggs = 'bacon'  # Creates a local variable 'eggs' (does not affect the global one)


def ham():
    print(eggs)  # Prints the global variable 'eggs'


eggs = 42  # Assigns 42 to the global variable 'eggs'
spam()  # Calls the spam function, changing the global 'eggs' to 'spam'
print(eggs)  # Prints 'spam' because the global variable was modified
