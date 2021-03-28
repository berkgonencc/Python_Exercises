# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""


# Your Code Below:

def last2(my_str):
    # Screen out too-short string case.
    if len(my_str) <= 2:
        return 0
    last_2 = my_str[-2:]
    count = 0
    for i in range(len(my_str) - 2):
        if last_2 == my_str[i] + my_str[i+1]:
            count += 1
    return count


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxxaaxx'))
print(last2('axxxaaxx'))

