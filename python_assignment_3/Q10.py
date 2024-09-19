# Write a Python program to count the frequency of words in a file.

import re
file=open("txt1.txt","r")
word=r'\w+'
sub=re.findall(word,file.read())
fr={}
for word in sub:
    word=word.lower()
    if word not in fr:
        fr[word]=1
    else:
        fr[word]+=1

for word,freq in fr.items():
    
    print(word,":",freq)