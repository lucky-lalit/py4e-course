# N = 5
#     *
#    **
#   ***
#  ****
# *****
# N = 5
# row = 0
# column = 0
def print_for(N):
    for row in range(N):
        # print('debug2')
        for space in range(N - (row + 1)):
            # print('debug1')
            print(' ', end = '')
        for column in range(row+1):
                # print('debug 3')
                print('*', end = '')
            # print('debug1',column)
            # print(column >= (N))
            # print(end = '')
            # if column >= N - 1:
            #     print('*')
        # print('debug 4','row :',row
        # ,'column :',column)
        print('')
    
    # row = row + 1

# print(print_for(5))
# print(print_for(4))
# print(print_for(3))

# row = 0
# column = 0
# N = 5
# space = 0
def print_while(N):
    row = 0
    while row < N:
        space = 0
        # print('debug70',row,space)
        while space < (N-(row+1)):
            # print('debug1',row,space)
            print(' ',end = '')
            # print('debug2')
            space = space + 1
            # column = 0
            # print('debug55',row,column)
        column = 0
        # print('debug56',row,column)
        while column < (row + 1):
            # print('debug3',row,column)
            # print('row',row)

            print('*', end = '')
            # print('debug4')
            column = column + 1

        # column = 0
        # print('debug5')
        print('')
        row = row + 1
        # column = column + 1
print(print_while(0))
print(print_while(3))
print(print_while(4))
print(print_while(5))
print(print_while(50))