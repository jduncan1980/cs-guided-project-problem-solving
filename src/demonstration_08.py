"""
Challenge #8:

Given an integer, write a function that returns "Even" for even integers and
"Odd" for odd integers.

Examples:
- parity(0) -> "Even"
- parity(1) -> "Odd"
- parity(2) -> "Even"
"""
def parity(input_int):
    # If integer mod 2 is 0, number is even
    if input_int % 2 == 0:
        return "Even"
    # Else, number is odd
    else:
        return "Odd"

print(parity(1))
print(parity(10))
print(parity(340))

