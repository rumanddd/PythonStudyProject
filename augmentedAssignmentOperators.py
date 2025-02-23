spam = 42 # Assign the value 42 to the variable spam
print(spam)

while spam < 50: # While spam is less than 50
    if spam == 42: # some condition
        spam += 1 # Add 1 to the value of spam
        continue # skip the rest of the code and move on to the next iteration
    print(spam)
    spam += 1 # Add 1 to the value of spam
    print(spam)
# It is the same as doing spam = spam + 1