def eggs(someParameter):
    someParameter.append('Hello')  # Modifies the list by adding 'Hello' at the end

spam = [1, 2, 3]  # Creates a list with initial elements [1, 2, 3]
eggs(spam)  # Calls the function and passes the list spam

print(spam)  # Prints the modified list, which now includes 'Hello'
