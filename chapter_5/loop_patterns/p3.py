# FOR N = 5
# *****
# ****
# ***
# **
# *

# print('*****')
# print('****')
# print('***')
# print('**')
# print('*')

# N = 5
# row = 0
# column = 0
def print_for(N):
    for row in range(N):
        for column in range(N - row):
            # print('debug1',row,column)
            print('*', end ='')
        print('')
        # print('debug1')
        # row = row + 1
        # column = column + 1

# print(print_for(0))
# print(print_for(3))
# print(print_for(4))
# print(print_for(5))

# N = 5
# column = 0
# row = 0
def print_while(N):
    row = 0
    while row < N:
        # print('debug1',row,column)
        column = 0
        while column < (N - row):
            # print('debug2',row,column)
            print('*',end = '')
            column = column + 1
        print('')
        # column = column + 1
        row = row + 1

print(print_while(0))
print(print_while(3))
print(print_while(4))
print(print_while(5))