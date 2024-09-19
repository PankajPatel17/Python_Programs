#Write a Python program to read last n lines of a file.

n=int(input("Enter Lines:"))

file=open("txt2.txt","r")
x=file.readlines()
for i in range(-n,0):
    print(x[i],end="")
file.close()