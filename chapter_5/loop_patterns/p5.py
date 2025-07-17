# N = 5

# *****
#  ****
#   ***
#    **
#     *
 
# row = 0
# column = 0
# N = 5
def print_pyramid(N):
    for row in range(N):
        for space in range(row):
            print(' ',end = '')
        for column in range(N - row):
            print('*',end = '')
        print('')


# print(print_pyramid(5))
# print(print_pyramid(4))
# print(print_pyramid(3))


# N = 5
# row = 0
# column = 0
# space = 0
def print_while(N):
    row = 0
    while row < N:
        space = 0
        while space < row:
            print(' ',end = '')
            space = space + 1
        column = 0
        while column < (N - row):
            print('*',end = '')
            column = column + 1
        print('')
        row = row + 1

print(print_while(0))
print(print_while(3))
print(print_while(4))
print(print_while(5))
print(print_while(125))