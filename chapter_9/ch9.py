# Practice 1
# cards = list()
# cards.append(1)
# cards.append(2)
# cards.append(3)
# print(cards)
# cards[0] = cards[1] + 3
# print(cards)

# Practice 2
# cabinet = dict()
# cabinet['Summer'] = 1
# cabinet['Winter'] = 21
# cabinet['MOnsoon'] = 54
# cabinet['Rainy'] = 51
# print(cabinet)
# cabinet['Winter'] = cabinet['Rainy'] + 10
# print(cabinet['Summer'])

# Practice 3
# new = dict()
# new['Hello'] = 2
# new['Hello'] = 4
# print(new)

# Practice 4
# count = dict()
# names = ['hello','my','name','is','my','hello','my']
# for name in names:
    # count[name] = count.get(name,0) + 1
    # if name not in count:
    #     count[name] = 1
    # else:
    #     count[name] = count[name] + 1
    # print(count[name],name)
# print(count)

# Pratice 5 Definite loops and Dictionasries
# count = {'hello' : 1,'my' : 2,'this' : 6,'loops' : 8}
# for key in count:
    # print(key,count[key], end = ' ')

# Retriving lists of keys and values 
# jjj = {'chuck' : 1,'fred' : 42,'jan' : 100}
# print(list(jjj))
# print(list(jjj.keys()))
# print(list(jjj.values()))
# print(list(jjj.items())) 

# Double Iteration
# jjj = {'chuck' : 10.5,'fred' : -55,'jan' : 100.p52}
# for aa,bb in jjj.items():
# #     print(aa,bb)

# bigcount = None
# bigword = None 
# for word,count in jjj.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count 
# print(bigword,bigcount)

# eng2sp = dict()
# eng2sp['Hello'] = 'world'
# print(eng2sp)

# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(len(eng2sp))

# vals = (eng2sp.values())
# print('uno' in vals)
# print(vals)

# word = 'brontosaurus'
# d = dict()
# for letter in word:
#     if letter not in d:
#         d[letter] = 1
#     else:
#         d[letter] = d[letter] + 1
# print(d)

# counts = {'chuck' : 1 , 'annie' : 42, 'jan': 100} 
# print(counts.get('march', 101))
# print(counts.get('annie' , 5))

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     d[c] = d.get(c,0) + 1
# print(d)

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])

# import string 
# print(string.punctuation)
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('Invlaid to open the file',fname)
#     exit()
# count =dict()
# for line in fhand:
#     line = line.strip()
#     # line = line.lower()
#     line = line.translate(line.maketrans({'a':string.punctuation}))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in count:
#             count[word] = 1
#         else:
#             count[word] = count[word] + 1
# print(count)

# line ='abcdefghi'
# print(line.translate({97 : 98,102 : None}))
# print('abcdefghi'.maketrans('a','b','f'))
# print('abcd')

counts = dict()
names = ['zqian','csev','cwen','csev','zqian','cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1    
print(counts)