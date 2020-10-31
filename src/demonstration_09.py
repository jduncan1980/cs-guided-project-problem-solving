"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"

# Determine if input is odd or even

    # if input length is odd, return 1 character
    # if input length is even, return middle 2 characters

"""
def is_even(num):
    return num % 2 == 0

def get_middle(input_str):
    # Get middle point of string
    string_middle = len(input_str) // 2
    # If String is even, return middle 2 digits, if odd only return middle
    if is_even(len(input_str)):
        return input_str[string_middle -1 : string_middle + 1]
    else:   
        return input_str[string_middle : string_middle + 1]


print(get_middle('test'))
print(get_middle('testing'))
print(get_middle('middle'))
print(get_middle('A'))