# Exercise 1: 
# Write a function called chop that takes a list and modifies it, removing the first and last elements, 
# and returns None. Then write a function called middle that takes a list and returns a new list that contains all but 
# the first and last elements.

def chop(inp_list):
    del inp_list[0]
    del inp_list[-1]
    

def middle(inp1_list):
    # t =inp1_list[1:-1]
    chop(inp1_list)
    return inp1_list


print(middle([1,2,3,4,5,6]))