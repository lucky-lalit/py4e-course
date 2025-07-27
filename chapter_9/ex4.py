# Exercise 4:
# Add code to the above program to figure out who has the most messages in the file. After all the data has been read
# and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and
# minimum loops) to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

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
# print(temp)
repeated_count = None
repeated_mailid = None
for word, count in mailid_dict.items():
    if repeated_count is None or count > repeated_count:
        repeated_count = count
        repeated_mailid = word

print(repeated_mailid, repeated_count)
