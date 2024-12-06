""" Explain the use of break and continue statement with suitable example ?
 
 
 The break and continue statements are used in loops (like for or while) to control the flow of execution.

 
 1. Break Statement

The break statement is used to exit the loop prematurely when a specific condition is met. Once the break statement is executed, the loop stops, and the program continues with the next statement after the loop.

Example: Using break to Exit a Loop"""

# Example: Break when a specific number is found
for num in range(1, 10):
    if num == 5:
        
        break  # Exits the loop when num == 5
    print(num)

print("Loop ended")

"""2. Continue Statement

The continue statement is used to skip the rest of the code in the current iteration and move to the next iteration of the loop. It does not exit the loop but instead skips any statements after it in the current iteration.

Example: Using continue to Skip Iterations"""

# Example: Skip even numbers
for num in range(1, 10):
    if num % 2 == 0:  # Check if the number is even
        continue  # Skip the current iteration
    print(num)

print("Loop ended")


