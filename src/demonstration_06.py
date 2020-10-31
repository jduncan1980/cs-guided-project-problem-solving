"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
# import re for working with regex
import re
def get_count(input_str):
    # Return the length of the string when all non-vowels are removed using regex
    return len(re.sub('[bcdfghjklmnpqrstvwxyz ]', '', input_str))

print(get_count('this is a string'))
print(get_count('aaa'))
print(get_count('afdssd'))