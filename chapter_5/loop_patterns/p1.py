# FOR N = 5 
# *****
# *****
# *****
# *****
# *****


def while_pattern(N):
    row = 0
    column = 0
    while row < N:
        # print('debug1')
        # print('*', end = '') # row 0 col 0 = *, row 1 col 0 = *
        # row = row + 1 # row 1, row 2
        column = 0
        while column < N : # remaing N - 1 col
            # print('debug2')
            print('*',end = '') # row 0 col 1 = *, row 0 col 2 = * 
            column = column + 1
        print('\n', end = '')
        row = row + 1

            

# print(while_pattern(0))
print(while_pattern(3))
# print(while_pattern(4))
# print(while_pattern(5))
# print(while_pattern(6))
# print(while_pattern(7))

def for_pattern(N):
    for row in range(N):
        for column in range(N ):
            # print('debug2')
            print('*', end = '')
        print('')

# print('my answer for 3',for_pattern(0))
# print('my answer for 3',for_pattern(3))
# print('my answer for 3',for_pattern(4))
# print('my answer for 3',for_pattern(5))
# print('my answer for 3',for_pattern(6))
# print('my answer for 3',for_pattern(7))

