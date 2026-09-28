"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Xander
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
monthly_goal = -1
while True:
    monthly_goal_str = input("How much money do you want to save every month? £")
    try:
        monthly_goal = int(monthly_goal_str)
    except ValueError:
        print(f"'{monthly_goal_str}' is not a valid integer!")
        continue
    if monthly_goal < 1:
        print("You need to provide a positive integer.")
        continue
    break


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
yearly_savings = monthly_goal * 12
print(f"With a monthly saving of £{monthly_goal}, you will save £{yearly_savings} per year!")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
yearly_savings_with_interest = yearly_savings * 1.08
interest_only = yearly_savings_with_interest - yearly_savings
print(f"When accounting for interest, you will have saved £{yearly_savings_with_interest:0.2f}. That's £{interest_only:0.2f} of interest!")
