"""Explain the following string inbuilt functions with syntax and example:"""

# Demonstrating len(), max(), min(), and isdigit()

# Using len()
sample_string = "Hello, Python!"
sample_list = [1, 2, 3, 4, 5]
print("Length of string:", len(sample_string))  # Output: 14
print("Length of list:", len(sample_list))      # Output: 5

# Using max()
numbers = [10, 20, 30, 40]
print("Maximum number:", max(numbers))          # Output: 40
print("Maximum character in 'Python':", max("Python"))  # Output: y

# Using min()
print("Minimum number:", min(numbers))          # Output: 10
print("Minimum character in 'Python':", min("Python"))  # Output: P

# Using isdigit()
numeric_string = "12345"
non_numeric_string = "123a"
print( numeric_string.isdigit())    # Output: True
print( non_numeric_string.isdigit()) # Output: False