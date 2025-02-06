# # Write a program that takes a list of integers as input and performs the following tasks:
# 1. Calculate the sum of all the numbers in the list.
# 2. Find the maximum and minimum values in the list.
# 3. Sort the list in ascending order.
# 4. Display the results to the user.

# Ask the user to enter a list of integers separated by a space.
numbers = input("Enter a list of integers separated by a space: ")

# Convert the input string into a list of integers.
numbers = list(map(int, numbers.split()))

# Calculate the sum of all the numbers in the list.
sum_numbers = sum(numbers)

# Find the maximum and minimum values in the list.
max_number = max(numbers)
min_number = min(numbers)

# Sort the list in ascending order.
sorted_numbers = sorted(numbers)

# Display the results to the user.
print(f"Sum of all numbers: {sum_numbers}")

print(f"Maximum value: {max_number}")

print(f"Minimum value: {min_number}")

print(f"Sorted list: {sorted_numbers}")
