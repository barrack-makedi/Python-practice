# define a function to help check if a number is even
def even_number(n):
    # define a base case in which 0 is even
    if n == 0:
        return True
    # define a base case in which 1 is odd
    elif n == 1:
        return False
    else:
        # Reduce the number by 2 and check again
        return even_number(n - 2)

# Function that returns "Even" or "Odd" based on the check
def the_result(n):
    # Use the even_number function and return a string according to the result
    return "Even number" if even_number(n) else "Odd number"

print(the_result(89)) 
print(the_result(19))