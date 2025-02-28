# Define function spam()
def spam():
    eggs = 'spam local'  # Local variable eggs inside spam()
    print(eggs)  # Prints 'spam local'

# Define function bacon()
def bacon():
    eggs = 'bacon local'  # Local variable eggs inside bacon()
    print(eggs)  # Prints 'bacon local'
    spam()  # Call spam() function
    print(eggs)  # Prints 'bacon local' again (unchanged in bacon())

# Global variable eggs
eggs = 'global'
bacon()  # Call bacon()
print(eggs)  # Prints 'global' (global variable remains unchanged)
