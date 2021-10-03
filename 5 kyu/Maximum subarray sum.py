# Instructions
"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


# My solution
def max_sequence(arr):
    max_sum = 0
    for i in range(len(arr)+1):
        for j in range(len(arr)-i+1):
            max_sum = max(max_sum, sum(arr[j:j+i]))
    return max_sum


# # Clever solution
# def maxSequence(arr):
#     lowest = ans = total = 0
#     for i in arr:
#         total += i
#         lowest = min(lowest, total)
#         ans = max(ans, total - lowest)
#     return ans
#
#
# def maxSequence(arr):
#     max,curr=0,0
#     for x in arr:
#         curr+=x
#         if curr<0:curr=0
#         if curr>max:max=curr
#     return max
