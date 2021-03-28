# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""


# Your Code Below:

def sequence(list_a):
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop otherwise it will give an error in some cases.
    for i in range(len(list_a)-2):
        if list_a[i] == 1 and list_a[i+1] == 2 and list_a[i+2] == 3:
            return True
    return False


print(sequence([1, 1, 2, 3, 1]))
print(sequence([1, 1, 2, 4, 1]))
print(sequence([1, 1, 2, 1, 2, 3]))
print(sequence([1, 2]))
print(sequence([]))
