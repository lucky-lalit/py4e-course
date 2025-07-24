
# fhand = open('.\\chapter_8\\mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words =line.split()
#     print(words[2])

# a = [1,2,3]
# b = [1,2,3]
# print(id(a),id(b))
# b[2] = 100
# print(a,b)

# fhand = open('.\\chapter_8\\mbox-short.txt')
# line_num = 0
# for line in fhand:
#     line_num = line_num + 1
#     words = line.split()
#     print('debug1',line_num,words)
#     if words[0] != 'From': 
#         continue
#     print(words[2])
    
# s = 'pining=for=the=fjords'
# t = s.split('=')
# print(t) 
# w = ' '.join(t)
# print(w)

list1 = [1,2,3,4,5]
print(list1[:]) 