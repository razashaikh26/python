"""Write a python code to find the maximum of two numbers using function with
arguments."""

# Function to find the maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Example usage
num1 = 10
num2 = 20
print("The maximum of", num1, "and", num2, "is:", find_max(num1, num2))

"""Explanation:
	1.	The function find_max(a, b) takes two arguments, a and b.
	2.	It compares the two values and returns the larger value using an if-else statement.
	3.	The result is printed by calling the function with specific numbers."""