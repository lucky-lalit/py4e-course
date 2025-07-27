# Exercise 3:
# Write a program to read through a mail log, build a histogram using a dictionary to count how many
# messages have come from each email address, and print the dictionary.

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

mailid_dict = {}
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
    word = words[1]
    if word not in mailid_dict:
        mailid_dict[word] = 1
    else:
        mailid_dict[word] = mailid_dict[word] + 1
print(mailid_dict)
