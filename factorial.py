# Function to calculate factorial using a loop statement
def jibuloop(n):
    # define the base case, hence start with 1 because the factorial of 0 is 1
    result = 1  
     # Multiply from 2 up to n, we start at 2 because multiplying by 1 changes nothing
    for i in range(2, n + 1): 
        #meaning result*i
        result *= i
    return result
print(jibuloop(5))
