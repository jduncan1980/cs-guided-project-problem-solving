"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a, n):
    # Get Last N Numbers by slicing 
    last = a[-n:]
    # Return "invalid" if n exceeds length of list or Empty list if n == 0
    if n > len(a):
        return 'invalid'
    elif n == 0:
        return []
    # Return last to caller
    return last

print(last([3, 4, 5, 6, 7], 2))
print(last([3, 4, 5, 6, 7], 3))
print(last([3, 4, 5, 6, 7], 0))
