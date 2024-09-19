# Write a Python program to unzip a list of tuples into individual lists

lst = [(1,'a',2), (3,4,'b'), ('c',5,6)]

lst1 = list(zip(*lst))

list1,list2,list3 = lst1

print("list 1 : ",list(list1))
print("list 2 : ",list(list2))
print("list 3 : ",list(list3))
