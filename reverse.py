# define a function to reverse a string 
def reverse_string(input_string):
    # Lets start with an empty string which will hold the new reversed string
    reversed_str = ""

    # lets loop through each character of the inputed string
    for char in input_string:
        # in order to reverse the characters in a string we put "char + reversed_str" to ensure first in last out scenario
        reversed_str = char + reversed_str

    return reversed_str

input_string = "hello"
print(reverse_string(input_string))
