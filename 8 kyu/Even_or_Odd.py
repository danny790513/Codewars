# Instructions
"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""


# My solution
def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'


# Best practices
# def even_or_odd(number):
#     # number % 2 will return 0 for even numbers and 1 for odd ones.
#     # 0 evaluates to False and 1 to True, so we can do it with one line
#     return "Odd" if number % 2 else "Even"

# # Clever solution
# def even_or_odd(number):
#     return ["Even", "Odd"][number % 2]
