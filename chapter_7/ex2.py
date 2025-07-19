# Exercise 2: 
# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point 
# number on the line. Count these lines and then compute the total of the spam confidence values from these lines. 
# When you reach the end of the file, print out the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519


fname = input('Enter the file name: ')
count = 0
fhand = open(fname)
sum = 0

# inp = fhand.read()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        # print(line)
        line1 = line.find(':')
        # print('debug1',line1)
        line2 = line[line1 + 1:]
        line3 = line2.strip()
        final_line = float(line3)
        # print(sum)
        sum = sum + final_line
        # print(sum)

        count = count + 1
# print(count)
print('Average spam confidence: ',sum/count)
