"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""
import datetime
def data_type(value):
    # Get the value type and convert to a string
    string_value = str(type(value)).lower()
    # Use '.split' method to remove portions of the string that aren't part of expected output
    result = string_value.split("'")[1]
    
    # date type has extra information, if type date remove that as well and return, otherwise return as is
    if result == "datetime.date":
        return result.split('.')[1]
    else:
        return result
    
print(data_type([1, 3]))
print(data_type('string'))
print(data_type({"a": "b"}))
print(data_type(1))
print(data_type(1.5))
print(data_type(True))
print(data_type(datetime.date(2018,1,1)))