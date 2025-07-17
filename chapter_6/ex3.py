# Exercise 3: 
# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as 
# arguments

def count(str,letter):
    count = 0
    first_i = None
    last_i = None
    i = 0
    for char in str:
        if char == letter:
            count = count + 1
            if first_i is None:
                # print('debug1')
                first_i = i
            # print('debug2')    
            last_i = i
        # print('debug3')    
        i = i + 1

    print(count)
    print(first_i,last_i)
    return count

count('demons are evil','e')