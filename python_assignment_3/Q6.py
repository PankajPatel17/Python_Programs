# Write a Python program to read a file line by line and store it into a list

file=open("txt2.txt","r")
l1=[]
for i in file:
    l1.append(i.strip())
print(l1)