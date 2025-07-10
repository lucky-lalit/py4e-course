# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an 
# error message. If the score is between 0.0 and 1.0, print a grade using the following table:

try:
    # print('Hello World')
    score=input("Enter Score: ")
    score=float(score)
    # print('user input',score,type(score))
    # print('if comd',score > 0.0 and score < 1.0)
    # print("if score >= 0.9 and score < 1.0:",score >= 0.9 and score < 1.0)
    # print('if score >= 0.8 and score < 1.0:',score >= 0.8 and score < 1.0)
    # print('elif score >=0.7 and score < 1.0:',score >=0.7 and score < 1.0,type(score >=0.7 and score < 1.0))
    # print('elif score >= 0.6 and score < 1.0:',type(score >= 0.6 and score < 1.0),score >= 0.6 and score < 1.0)
    # print('elif score < 0.6 and score >0.0:',type(score < 0.6 and score >0.0),score < 0.6 and score >0.0)
    if score >= 0.9 and score < 1.0:
        print('A')
    elif score >= 0.8 and score < 1.0:
        print('B')
    elif score >=0.7 and score < 1.0:
        print('C')
    elif score >= 0.6 and score < 1.0:
        print('D')
    elif score < 0.6 and score > 0.0:
        print('F')

    else:
        print('Bad score')

except:
    print('Bad score')



























# print('Hello world')
# score=input('Enter score: ')
# score=float(score)
# print(type(score))
# print('if conditon',score > 0.0 and score < 1.0)
# print('elif 1',score  >= 0.9 and score < 1.0)
# if score > 0.0 and score < 1.0:
#     print("in range")
# if score  >= 0.9 and score < 1.0:      
#         print('A')
# # int('a')

# else:
#      print("Bad score")



 





# # score=input("Enter Score: ")

# # score == "perfect"
# # print("bad Score")
# # score=float(score)

# # if score > 0.0 and score < 1.0:
      
                


# # # for (0.0<score<=1.0):
# # # else:
# # # if score  >= 0.99:
# # # print('A')
# # # elif score >= 0.8:
# # # print('B')
# # # if score >=0.7:
# # # print('C')
# # # elif score >= 0.6:
# # # print('D')
# # # elif score  <  0.6:
# # # print('F')
# # # if score == "perfect":
# # # print("bad Score")
# # # elif score == 10:
# # # print("Bad Score")
