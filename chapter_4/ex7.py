# Exercise 7: 
# Rewrite the grade program from the previous chapter using a function called computegrade 
# that takes a score as its parameter and returns a grade as a string.

def computegrade(score):
    
    if score >= 0.9 and score < 1.0:
        return 'A'
    elif score >= 0.8 and score < 1.0:
        return 'B'
    elif score >=0.7 and score < 1.0:
        return 'C'
    elif score >= 0.6 and score < 1.0:
        return 'D'
    elif score < 0.6 and score > 0.0:
        return 'F'  
    else:
        return 'Bad score'





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
    print(computegrade(score))
except:
    print('Bad score')


