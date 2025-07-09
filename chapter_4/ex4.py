score = input('Enter score: ')
score = float(score)
print('debug1',score >= 0.9 and score < 1.0)
print('debug2',score >= 0.8 and score < 1.0)
print('debug3',score >= 0.7 and score < 1.0)
print('debug4',score >= 0.6 and score < 1.0)
print('debug5',score < 0.6 and score < 1.0)

def computegrade(score):
    # if score > 0.0 or score > 9.9:
    #     print('In range')
    if score >= 0.9 and score < 1.0:
       
        return 'A'
        
    elif score >= 0.8 and score < 1.0:
        return 'B'
    elif score >= 0.7 and score < 1.0:
        return 'C'
    elif score >= 0.6 and score < 1.0:
        return 'D'
    elif score < 0.6 and score > 0.0:
        return 'F'
    else:
        return 'Bad score'
print(computegrade(0.95),score >= 0.9 and score < 1.0)
print(computegrade(0.8),score >= 0.9 and score < 1.0)

# print(computegrade(10.0))
# print(computegrade(0.95))
# print(computegrade(0.95))
# print(computegrade(0.95))
# print(computegrade(0.95))