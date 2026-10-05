# Worksheet 1.2: Task 2 Solution

import sys

import util

numbers = util.read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers were entered")

numbers_sorted = sorted(numbers)

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)
median = numbers_sorted[len(numbers) // 2]

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")
