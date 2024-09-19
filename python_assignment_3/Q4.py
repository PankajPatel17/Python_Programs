# Write a Python program to read first n lines of a file.

n=int(input("Enter lines:"))
file=open("txt2.txt","w")
file.write("This is file management.\nThis is file management.\nThis is file management.\nThis is file management.\nThis is file management.\nThis is file management.\nThis is file management.\nThis is file management.")

print("File successfully written")
file=open("txt2.txt","r")
x=file.readlines()

for i in range(0,n):
    print(x[i],end='')
file.close()