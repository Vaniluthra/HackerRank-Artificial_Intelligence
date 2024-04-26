import re
from collections import Counter
from string import ascii_lowercase

def words(text):
    return re.findall(r'(?:[a-z]+[a-z\'\-]?[a-z]|[a-z]+)', text.lower())

def alternate_words(word):
    lst=[]
    for i in ascii_lowercase:
        for j in range(len(word)+1):  
            lst.append(word[:j]+i+word[j:])
    for i in range(1,len(word)):     
        lst.append(word[:i-1]+word[i]+word[i-1]+word[i+1:])
    for i in range(len(word)):  
        lst.append(word[:i]+word[i+1:])
    for i in ascii_lowercase:  
        for j in range(len(word)):
            lst.append(word[:j]+i+word[j+1:])
    return lst

def valueOf(word):
    return Vocabulary[word]

def spelled_word(word):
    suggestions = set(alternate_words(word)).intersection(set(Vocabulary))
    if len(suggestions) > 0:
        maxScoreWord = max(suggestions, key = valueOf)
        return sorted([i for i in suggestions if Vocabulary[i] == Vocabulary[maxScoreWord]])[0]
    return (word)

Vocabulary = Counter(words(open('corpus.txt').read()))
for i in range(int(input())):
    word = input().strip().lower()
    if word in Vocabulary:
        output = word
    else:
        output = spelled_word(word)
    print(output)
