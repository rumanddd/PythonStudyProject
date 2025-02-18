def spam():
    global eggs
    eggs = 'spam'  # this is the global variable

eggs = 'global'
spam()
print(eggs)

# This code will print 'spam'