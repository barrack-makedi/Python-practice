#define a function that takes a number n
def recursivefaco(n):
    #define the base case which is 1, as the factorial of both 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    #this is the start of the recursive case
    else:
        #we take the number n and multiply it by the factorial of numbers before it
        return n * recursivefaco(n - 1)
print(recursivefaco(5)) 
