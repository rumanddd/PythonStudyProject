spam = ['Apples', 'Bananas', 'Cat Food', 'Dog']
def newList(list):
    newString = ''
    for i in list:
        newString = newString + str(i)
        if list.index(i) == (len(list)-2):
            newString = newString + ', and '
        elif list.index(i) == (len(list)-1):
            newString = newString
        else:
            newString = newString + ', '
    return newString
print(newList(spam))
