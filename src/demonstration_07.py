"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def repeat_it(input_str):
    # Create empty list placeholder
    string_list = []
    # Iterate over the string using enumerate to gain access to index
    for index, value in enumerate(input_str, 1):
        # Append the current value multiplied by the index number and capitalized to string_list
        string_list.append(str.capitalize(value * index))
        
    # Join string_list back in to a string using '-' as a seperator
    return '-'.join(string_list)

print(repeat_it('abcd'))
print(repeat_it("RqaEzty"))
print(repeat_it("cwAt"))