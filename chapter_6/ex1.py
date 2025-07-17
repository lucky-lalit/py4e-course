# Exercise 1: 
# Write a while loop that starts at the last character in the string and works its way backwards to the first 
# character in the string, printing each letter on a separate line, except backwards

fruit = "banana" 
# index = len(fruit) - 1
# while index < len(fruit) and index >= 0:
# #     letter = fruit[index]
# #     print(letter)
#     print(index)
#     index = index - 1

# index = len(fruit)-1
# for i in range(index,-1,-1):
#     letter = fruit[i]
#     # print(i)
#     print(letter)
    
index = len(fruit) - 1
for char in fruit:
    print(fruit[index],char)
    index = index - 1