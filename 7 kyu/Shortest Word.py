# Instructions
"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


# My solution
def find_short(s):
    # your code here
    l = min(list(len(word) for word in s.split()))
    return l  # l: shortest word length

# # Clever solution
# def find_short(s):
#     l = min(map(len, s.split()))
#     return l

# def find_short(s):
#     l = min(s.split(), key=len) # finds the shortest string in the list
#     return len(l) # returns shortest word length
