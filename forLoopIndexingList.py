supplies = ['pencils', 'staplers', 'pins', 'glues' ] # Define a list called 'supplies' with different items
for i, item in enumerate(supplies): # Loop through the range of numbers from 0 to the length of 'supplies' - 1
    print('Index '+ str(i) + ' in supplies are ' + supplies[i]) # Print the index and the corresponding item in the list
    # The enumerate() function is useful if you need both the item and the item’s index in the loop’s block.