# Exercise 1
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

word_count = dict()
fname = input("Enter  a file: ")
fhand = open(fname)
for line in fhand:
    line = line.strip()
    words = line.split()

    for word in words:
        # for words in line:
        #     print(words)
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1
print(word_count)
# words = line_strip.split()
# print(words)
# result[words] = True
# print(result)
