# FOR N = 5
# *
# **
# ***
# ****
# *****

def while_pattern(N):
 
    column = 0
    row = 0
    while row <= N-1 :
        # print('debug1')
        # print('*')
        # row = row + 1
        # i = i + 1
        # if row < N:
        column = 0

        # print('debug1','row',row,'column',column)
        while column < row + 1:
                # if column < N:
            # print('debug2','row',row,'column',column)    
            print('*',end = '')

            column = column + 1
            # while column == N -1:
        print('')
        row = row + 1
        # column = 0

print(while_pattern(3))


def for_pattern(N):
    # row = 0
    for row in range(N):
        # row = row + 1
        for column in range(row + 1):
            print('debug2',row,column)
            print('*', end = '')
        print('')

# print('my answer for 3',for_pattern(0))
# print('my answer for 3',for_pattern(5))
# print('my answer for 3',for_pattern(4))
# print('my answer for 3',for_pattern(5))
# print('my answer for 3',for_pattern(6))
# print('my answer for 3',for_pattern(7))