# Exercise 2: 
# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and 
# minimum of the numbers instead of the average.

smaller = None
larger = None
while True:
    
    inp = input('Enter a number: ')
    # print(type(inp))
    # print('debug1')
    # try:
    # inp_num = inp(int)
    if inp == 'done':
        # print('debug2')
        break
    try:
        inp_num = int(inp)
    except:
        print('Invalid input')
        continue
    # print(type(inp_num))
    # print('debug3',larger)
    if (larger is None) or (inp_num > larger):
        # print('debug4',larger)
        larger = inp_num
        # print('debug3',larger)
    
    if (smaller is None) or (inp_num < smaller):
        # print('debug5',smaller)
        smaller = inp_num
        # print('debug6',smaller)
    # except:
        # print('debug7')
        # print('Invalid inp')
# print('debug8')
print(larger,smaller)