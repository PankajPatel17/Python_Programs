# Write a Python program to find the second smallest number in a list.

lst = [1,23,2,3,4,5,6,7,8,9,10]

lst1=list(set(lst))
lst1.sort()
second_smallest = lst1[1]
print(second_smallest)

