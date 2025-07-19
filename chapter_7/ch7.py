# practice 1
# fhand = open('mbox.txt','r')
# count = 0
# for line in fhand:
#     count = count + 1
# print('The count of the file: ',count)
# print(fhand)

# practice 2
# fhand = open('mbox-short.txt','r')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# pratice 3 --> printed lines start with from
# fhand = open('mbox-short.txt','r')
# for line in fhand:                                        
#     if line.startswith('From'):
#         print(line)

# practice 4 --> removes the space from end of the lines 
# fhand = open('mbox-short.txt','r')
# for line in fhand:
#     line = line.strip()
#     if line.startswith('From'):
#         print(line)

# practice 5 --> used continue to avoid extra reading or scanning 
# fhand = open('mbox-short.txt','r')
# for line in fhand:
#     line = line.strip()
#     if not line.startswith('From'):
#         continue
#     print(line)

#  practice 6 --> instead of startswith here we used in
# fhand = open('mbox-short.txt','r')
# for line in fhand:
#     line = line.strip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)

# practice 7 --> taking user input and coutning the no. of times the repetation of word
# fname = input('Enter a file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count =count + 1
# print('Ther were ' , count , 'of word subject in' , fname )

# practice 8 --> solve the problem where the user enter invlaid file
# fname = input('Enter a file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('The File cannot be opened',fname)
#     quit()
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count =count + 1
# print('Ther were ' , count , 'of word subject in' , fname )
