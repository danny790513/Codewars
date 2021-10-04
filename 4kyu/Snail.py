# Instructions
"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].


"""


# My final solution
def snail(snail_map):
    ans = []
    while snail_map:
        ans += snail_map.pop(0)
        snail_map = list(map(list, zip(*snail_map)))[::-1]
    return ans


# My solution
def snail(snail_map):
    ans = []
    while snail_map:
        ans += snail_map.pop(0)
        if snail_map:
            lst_1 = []
            for i in range(len(snail_map[0])-1, -1, -1):
                lst_2 = []
                for j in range(len(snail_map)):
                    lst_2.append(snail_map[j][i])
                lst_1.append(lst_2)
            snail_map = lst_1
    return ans


# Clever solution
def snail(snail_map):
    ans = []
    while snail_map:
        ans += snail_map.pop(0)
        snail_map = list(map(list, zip(*snail_map)))[::-1]
    return ans

# test case
array_1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected_1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(snail(array_1))
#
# array_2 = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# expected_2 = [1,2,3,4,5,6,7,8,9]
# print(snail(array_2))