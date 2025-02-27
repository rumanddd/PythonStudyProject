# Creating a sample list
import random

my_list = [5, 3, 8, 1, 2, 1]

# Adding elements
my_list.append(6)  # Adds 6 to the end of the list
my_list.insert(2, 10)  # Inserts 10 at index 2

# Removing elements
my_list.remove(3)  # Removes the first occurrence of 3
popped_value = my_list.pop()  # Removes and returns the last element
popped_index = my_list.pop(1)  # Removes and returns the element at index 1

# Modifying the list
my_list.sort()  # Sorts the list in ascending order
my_list.reverse()  # Reverses the order of the list

# Finding elements
index_of_8 = my_list.index(8)  # Returns the index of the first occurrence of 8
count_of_1 = my_list.count(1)  # Returns the number of times 1 appears in the list

# Copying and extending lists
copy_list = my_list.copy()  # Returns a shallow copy of the list
my_list.extend([7, 9])  # Adds elements from the given iterable to the end

# Clearing the list
my_list.clear()  # Removes all elements from the list

# List comprehension (not a method, but useful for transformations)
squared_list = [x**2 for x in copy_list]  # Creates a new list with squares of elements

# Enumerate example
enum_list = list(enumerate(copy_list))  # Returns a list of tuples with index and values

# Shuffling the list
random.shuffle(copy_list)  # Randomly shuffles the elements in the list

# Random choice
random_element = random.choice(copy_list)  # Selects a random element from the list

# Filtering the list using filter function
filtered_list = list(filter(lambda x: x % 2 == 0, copy_list))  # Returns only even numbers

# Checking membership
contains_five = 5 in copy_list  # Checks if 5 is in the list

# Getting the length of the list
list_length = len(copy_list)  # Returns the number of elements in the list

# Maximum and minimum values
max_value = max(copy_list)  # Returns the maximum value in the list
min_value = min(copy_list)  # Returns the minimum value in the list

# Summing elements
total_sum = sum(copy_list)  # Returns the sum of all elements in the list

# Creating a set from a list (removes duplicates)
unique_elements = list(set(copy_list))  # Converts list to set and back to remove duplicates

# Finding the difference between two lists
difference_list = list(set(copy_list) - set(my_list))  # Elements in copy_list but not in my_list

print(my_list) # Prints the original list
print(index_of_8) # Prints the index of 8
print(count_of_1) # Prints the count of 1
print(copy_list) # Prints the copied list
print(squared_list) # Prints the list with elements squared
print(enum_list) # Prints the list enumerating the index and values
print(random_element) # Prints a random part of the list
print(filtered_list) # Prints the filtered list as set so it will print out only the even numbers
print(contains_five) # Prints True or False whether 5 is in the list
print(list_length) # Prints the length of the list
print(max_value) # Prints the maximum value inside the list
print(min_value) # Prints the minimum value of the list
print(total_sum) # Prints the total sum of all numbers in the list
print(unique_elements) # Prints the unique elements
print(difference_list) # Prints the difference list