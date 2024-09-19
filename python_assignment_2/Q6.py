#  Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

lst = ["aba", "xyz", "a", "xyx", "ab", "cdc","dad"]

count = 0

for i in lst:
    if len(i)>=2 :
        if i[0] == i[-1]:
            count = count + 1

print(count)
