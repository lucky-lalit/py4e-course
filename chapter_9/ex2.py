# Exercise 2:
# Write a program that categorizes each mail message by which day of the week the commit was done. To do
# this look for lines that start with “From”, then look for the third word and keep a running count of each of the days
# of the week. At the end of the program print out the contents of your dictionary (order does not matter)
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

commit_days = {}
fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    # if not line.startswith('From'):
    #     continue
    line.strip()
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    # print('debug1',words)
    # print(words[2])
    word = words[2]
    if word not in commit_days:
        commit_days[word] = 1
    else:
        commit_days[word] = commit_days[word] + 1
print(commit_days)

# if words not
