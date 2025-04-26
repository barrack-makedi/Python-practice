# define a function to find the sum of digits of a number of your choice
def sumya_digo(n):
    # define the Base case if the number is a single digit return that number
    if n < 10:
        return n
    else:
        # To get the last digit we will use the modulus operator which will give us a remainder when that number is divided by 10
        # The next part is to use integer division which assists us in lowering the number as each step progresses
        # Hence when we have a number firstly we get and remove the last number, then the current number is what is forwaded to the next step and the process is repeated again till we reach 0
        return (n % 10) + sumya_digo(n // 10)
print(sumya_digo(1234))  