# Instructions
"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""
# My solution
from collections import defaultdict


# def count(string):
#     count = defaultdict(int)
#     for ch in string:
#         count[ch] += 1
#     return count


# Clever solution
from collections import Counter


def count(string):
    return Counter(string)


def count(s):
    return {x: s.count(x) for x in set(s)}
