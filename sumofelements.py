# define the function
def sum_ya_elements(element):
    # define the base case/ the list is empty
    if not element:
        return 0
    else:
        #take the first element which is zero and add it to the next element
        return element[0] + sum_ya_elements(element[1:])
elementsare= [2, 4, 6, 8]
#display the sum
print(sum_ya_elements(elementsare))  

