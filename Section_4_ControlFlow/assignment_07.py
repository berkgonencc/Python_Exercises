# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:


def string_match(str_a, str_b):
    shorter = min(len(str_a), len(str_b))
    count = 0
    for i in range(shorter - 1):
        if str_a[i:i+2] == str_b[i:i+2]:
            count += 1
    return count


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))