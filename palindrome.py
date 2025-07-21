# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. 
# For example, 545 is a palindrome number.

def is_palindrome(number):
    if number < 0:
        return False  # Negative numbers are not palindromes

    original_string = str(number)           # Convert number to string (e.g., "121")
    reversed_string = original_string[::-1] # Reverse it using slicing (e.g., "121")

    if original_string == reversed_string:
        return True
    else:
        return False

# Example usage:
print(is_palindrome(121))   # True
print(is_palindrome(123))   #  False
