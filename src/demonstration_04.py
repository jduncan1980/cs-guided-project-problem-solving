"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""

# first pass solution
def emotify(txt):
    #store the key/value pairs of the required for swapping out the text in dictionary
    data = {
        "smile": ":D",
        "grin": ":)",
        "sad": ":(",
        "mad": ":P"
    }
    
    #iterate over the dictionary items extracting the key and value
    for k, v in data.items():
        # set an updated string using '.replace' to return each new string with the new substring substituted
        txt = txt.replace(k, v)
    
    # return our new string
    return txt

# second pass - optimized solution
def emotify2(txt):
    #store the key/value pairs of the required for swapping out the text in dictionary
    data = {
        "smile": ":D",
        "grin": ":)",
        "sad": ":(",
        "mad": ":P"
    }
    
    start_of_string = txt[:8]
    end_of_string = txt[8:]
    
    full_string = start_of_string + data[end_of_string]
    return full_string
    
    # Get the data/substring of txt from start to index 7 (8 - 1) [:8]
    

print(emotify("Make Me smile"))
print(emotify("Make Me grin"))
print(emotify("Make Me sad"))
print(emotify("Make Me mad"))
print(emotify2("Make Me smile"))
print(emotify2("Make Me grin"))
print(emotify2("Make Me sad"))
print(emotify2("Make Me mad"))
