#Write a python program to find the longest words.

import re

l1="dfvdv vfvss qffv dsfrvv helooooo"
word=r'\w+'
sub=re.findall(word,l1)
max_word=max(sub,key=len)
print(max_word)