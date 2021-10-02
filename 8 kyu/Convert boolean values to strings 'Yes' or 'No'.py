# Instructions
"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""


# My solution
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


# Best practices
# def even_or_odd(number):
#     # number % 2 will return 0 for even numbers and 1 for odd ones.
#     # 0 evaluates to False and 1 to True, so we can do it with one line
#     return "Odd" if number % 2 else "Even"

# # Clever solution
# def even_or_odd(number):
#     return ["Even", "Odd"][number % 2]
