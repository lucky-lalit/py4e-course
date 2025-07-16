# Exercise 1: 
# Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, 
# print out the total, count, and average of the integers. If the user enters anything other than a integers, detect 
# their mistake using try and except and print an error message and skip to the next integers.

# count = 0
# # try:
# # inp = (input('Enter a number: '))
# # answer = float(inp)
# while True:
#         inp = (input('Enter a number: '))
#         answer = float(inp)
#         if answer > 0:
#             num = answer
#             count = count + 1
#             Total = num + answer 
#             Avg = Total / count

# except:
#     if answer == 'done':
#         print(Total,count,Avg)



# except:
#     print('Invalid input')

count = 0
avg = 0
sum = 0
while True:
    inp =input('Enter a numner: ')
    # print(type(inp))
    # inp = int(inp)
    # print('debug1')?
    if inp == 'done': 
        break
    # if  int(inp):
        # count = count + 1
    # print('debug2',count)
    # count = count + 1
    # print('debug3',count)
    try:

        num_inp = int(inp)
    except:
        # print('debug4')?
        print('Invalid input')
        continue
        # print('debug3')
        # count = count + 1
        print('debug10')
    sum = sum + num_inp
    # print('debug45',count)?
    count = count + 1
    
    # avg = sum / count
    # sum = sum + inp
    # avg = sum/count
# print('debug5')
# count = count - 1
avg = sum / count 
print(sum,count,avg)
        # break
