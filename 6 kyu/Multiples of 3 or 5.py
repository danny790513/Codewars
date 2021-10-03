# Instructions
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
Courtesy of projecteuler.net (Problem 1)
"""


# My solution
def solution(number):
    if number < 0:
        return 0
    target = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            target.append(i)
    return(sum(target))


# Clever solution
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# # Clever solution
# def solution(number):
#     a3 = (number-1)/3
#     a5 = (number-1)/5
#     a15 = (number-1)/15
#     result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
#     return result
#
# # Clever solution
# def solution(number):
#     threes = range(3, number, 3)
#     fives = range(5, number, 5)
#     return sum(list(set(threes + fives)))
