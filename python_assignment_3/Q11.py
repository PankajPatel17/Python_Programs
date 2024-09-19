# Write a Python program to write a list to a file.

l2=[1,2,3,4,5]

file=open("txt1.txt","w")

for i in l2:
    file.write(str(i))
file.close()
print("Done")
