"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # Convert string to a list of ints
    int_list = [int(num) for num in input_str.split(' ')]
    # Get largest digit by calling max() on int_list
    high = max(int_list)
    # Get smallest digit by calling min() on int_list
    low = min(int_list)
    # Convert highest and lowest to string
    string_result = "%d %d" % (high, low)
    # Return string to caller
    return string_result

print(max_and_min("1 2 3 4 5"))
print(max_and_min("1 2 -3 4 5"))
print(max_and_min("1 9 3 4 -5"))