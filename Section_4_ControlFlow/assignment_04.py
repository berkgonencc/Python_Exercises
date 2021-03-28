# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""


# Your Code Below:

def grow_string(my_str):
    new_str = ""
    for i in range(len(my_str)):
        new_str = new_str + my_str[:i+1]
    return new_str


print(grow_string('Berk'))
