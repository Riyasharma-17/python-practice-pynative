# Exercise 5: Create a copy of a list and modify the copy.

original_list = [10, 20, 30]
print("Original list initially:", original_list)

# Create a copy using slicing
# This is a common and concise way to create a shallow copy
copied_list = original_list[:]

# Modify the copied list
copied_list.append(40)
copied_list[0] = 100

print("Original list after modifying copy:", original_list)
print("Copied list after modification:", copied_list)

# Demonstration using list() constructor
another_copy = list(original_list)
another_copy.append(50)
print("\nOriginal list after another_copy modification:", original_list)
print("Another copied list:", another_copy)

# Demonstration using .copy() method (Python 3+)
third_copy = original_list.copy()
third_copy[0] = 999
print("\nOriginal list after third_copy modification:", original_list)
print("Third copied list:", third_copy)


# Exercise 6: Combine two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined List:", combined_list)

# Method 2: Using the extend() method (modifies list_a in-place)
temp_list = [1, 2]
temp_list.extend(list2)
print("Combined list (using .extend() on temp_list):", temp_list)


# Exercise 7: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)


# Exercise 8: Remove Duplicates from list

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
unique_elements_set = set(list_with_duplicates)
unique_list = list(unique_elements_set)
print(f"Original list: {list_with_duplicates}")
print(f"List with unique elements: {unique_list}")


# Exercise 9: Remove all occurrences of a specific item from a list
item_list = [1, 2, 3, 2, 4, 2, 5]
item_to_remove = 2
filtered = [item for item in item_list if item != item_to_remove]
print(f"List after removing {item_to_remove}:", filtered)

