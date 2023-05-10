from collections import Counter
mylist=[1,1,1,1,1,2,2,2,2,2,2,4,4,4,4,4,5,5,5,5]
print(Counter(mylist))
l1=['a','a',10,10,10]
print(Counter(l1))
# count the words on the sentence
sentence="How many Times does each word show up in the sentence with a word"
print(Counter(sentence.split()))
letters="aaaabbbbbcccccddddddd"
c=Counter(letters)
print(c)
print(list(c))