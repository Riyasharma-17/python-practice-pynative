#Q3. Given a list of numbers. write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

print("Squared list:", squared_numbers)
