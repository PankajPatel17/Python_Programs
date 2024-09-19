# Write a Python program to append text to a file and display the text.

file=open("txt1.txt","a")
file.write("This file is now appended")
file=open("txt1.txt","r")
print(file.read())
file.close()
