"""
Source: edX, Python for Data Science, UCSanDiegoX

Goal: Instantiate a dictionary, and for every word in the file, add to 
the dictionary if it doesn't exist. If it does, increase the count.

"""

# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens

import collections

file=open('98-0.txt', encoding="utf8")

# if you want to use stopwords, here's an example of how to do this
stopwords = set(line.strip() for line in open('stopwords'))

# initialize dictionary data structure
wordcount={}

# Hint: To eliminate duplicates, remember to split by punctuation, 
# and use case demiliters. The functions lower() and split() will be useful!

# iterate through each line
for line in file:
    for word in line.split():
        word = word.lower()
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace("\"","")
        word = word.replace("“","")
        
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

counter = collections.Counter(wordcount)

top_ten = counter.most_common(10)

for word, count in counter.most_common(10):
 	print(word, ": ", count)
