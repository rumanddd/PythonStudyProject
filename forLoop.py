total = 0
for num in range(101):
    total = total + num
    print(total)    # The for loop executes total = total + num  100 times.

    #In each loop:
# When num = 0: total = 0 + 0 = 0
# When num = 1: total = 0 + 1 = 1
# When num = 2: total = 1 + 2 = 3
# When num = 3: total = 3 + 3 = 6
# And so on until num = 100