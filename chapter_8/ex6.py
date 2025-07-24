# Exercise 6:
# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the
# numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and
# use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0
num_list = list()
while True:
    inp = input("Enter a number: ")

    # for num in inp:
    if inp == "done":
        # print('debug5')
        # print('Maximum: ',max(num_list))
        # print('Minimum: ',min(num_list))
        break
        # break
    # print('debug2',type(inp))
    # num = int(inp)
    # print('debug1',num)
    # if num == 'done':
    #     break

    # try:
    # if (num > 0) or (num < 0):
    # except:
    # print('please enter a number')
    num_list.append(float(inp))
print("Maximum: ", max(num_list))
print("Minimum: ", min(num_list))
# print(num_list)

# print('Maximum: ',max(num_list))
# print('Minimum: ',min(num_list))
# break
