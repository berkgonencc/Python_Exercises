# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""


# Your Code Below:

def sum78(my_list):
    flag = False
    total = 0

    for i in range(len(my_list)):
        if my_list[i] == 7:
            flag = True

        if not flag:
            total += my_list[i]

        if my_list[i] == 8:
            flag = False

    return total


print(sum78([1, 2, 2]))
print(sum78([1, 2, 2, 7, 99, 99, 8]))
print(sum78([1, 1, 7, 8, 2]))

