#1Q 
# my_list = [10, 20, 30, 40, 50]
# Perform following list manipulation operations on given list

my_list = [10, 20, 30, 40, 50]
print("Initial list:", my_list)

# Change Element: Change the second element of a list to 200 and print the updated list.
my_list[1] = 200
print("after change", my_list)

# Append Element: Add 600 o the end of a list and print the new list.
my_list.append(600)
print("List after appending 600:" , my_list)

# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
my_list.insert(2,300)
print("List after inserting 300 at index 2:", my_list)

# Remove Element (by value): Remove 600 from the list and print the list.
my_list.remove(600)
print("List after removing 600 (by value):" , my_list)

# Remove Element (by index): Remove the element at index 0 from the list print the list.
del my_list[0]
print("List after removing element at index 0:" , my_list)