# z = (1,2,3,4,5,6)
# z[2] = 5
# print(z)

# a = 10
# b = 20
# (a,b) = (b,a)
# print(a,b)

# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for (k,v) in d.items():
#     print(k,v)
# tupes = d.items()
# print(tupes)

# print((1,56,16) > (0,74,1))

# d = {'a' : 10, 'c' : 22, 'b':1,'a' : 15}
# print(d.items(),type(d.items()))
# print(sorted(d.items()))
# for (k,v) in sorted(d.items()):
#     print(k,v)

# d = {'a' : 10, 'c' : 22, 'b':1,'a' : 15}
# temp = list()
# for k,v in d.items():
#     temp.append((k,v))
# print(temp)
# temp = sorted(temp)
# print(temp)
# temp = sorted(temp,reverse = False)
# print(temp)
# temp = sorted(temp,reverse = True)
# print(temp)

# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1

# lst = list()
# for k,v in counts.items():
#     newtup = (v,k)
#     lst.append(newtup)

# lst = sorted(lst,reverse=True)

# for v,k in lst[:10]:
#     print(k,v)


# t ='a','b','c','d','e'
# print(t)
# t1 = ('a',)
# print(t1)

# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))

# t.sort(reverse=True)

# res = list()
# for length, word in t:
#     res.append(word)

# print(res)

# d = {'a':10, 'b':1, 'c':22}
# l = list()
# for key, val in d.items() :
#     pass
#     l.append((val,key))
#     l.sort(reverse=False)
# print(l)

# import string
# fhand = open('romeo-full.txt')
# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1

# # Sort the dictionary by value
# lst = list()
# for key, val in list(counts.items()):
#     lst.append((val, key))

# lst.sort(reverse=True)

# for key, val in lst[:10]:
#     print(key, val)

# import timeit

# # Tuple access
# print("Tuple access time:")
# print(timeit.timeit('x[1]', setup='x=(1,2,3)', number=1000000))

# # List access
# print("List access time:")
# print(timeit.timeit('x[1]', setup='x=[1,2,3]', number=1000000))

# my_dict = {}

# key1 = (1, 2)
# key2 = [1, 2]  # ❌ Unhashable type: list

# my_dict[key2] = "Tuple as key"
# print(my_dict)

# import sys

# t = (1, 2, 3)
# l = [1, 2, 3]

# print("Tuple size:", sys.getsizeof(t))
# print("List size :", sys.getsizeof(l))

# print(print<type)

# print(1<'a')

print([1,2]<[2,2])
# print([1,2]<(1,2))
print((1,2)<(2,1))
# print({1:2}<{2:1})
print(3>4.0)