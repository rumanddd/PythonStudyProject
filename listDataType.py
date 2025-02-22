spam = ["cat", "dog", "bat", "frog"] # This assigns spam 1 value, which is a list of 4 strings
print(spam) # Will print out the whole list
print(spam[0]) # Will print out the first element of the list

spam[0] = "fly" # Will change the first element of the list
print(spam)

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]] # This assigns spam 1 value, which is a list of 2 lists
print(spam [1]) # Will print out the second element of the list
print(spam [1][0]) # Will print out the first element of the second element of the list
print(spam [-2]) # Will print out the second element of the list
print(spam [1][1:4]) # Will print out the second element of the list from index 1 to index 4
# spam[1:4] is a list with a slice (two integers)

print(len(spam)) # Will print out the length of the lists indexes

spam[1] = spam[1] + ['new item'] # Will append the new item to the second element of the list
print(spam)

spam = [1,2,3] + ['A', 'B', 'C'] # Will append the new item to the second element of the list
print(spam)

spam = ['X', 'Y', 'Z'] * 3
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant']
del spam [2]
print(spam)

