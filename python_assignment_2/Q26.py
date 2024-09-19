#Write a Python program to replace last value of tuples in a list.

lst = [(1,2,3),(4,5,6),(7,8,9)]

new_value = 40

new_lst = []
for i in lst:
    new_tuple = i[:-1] + (new_value,)
    new_lst.append(new_tuple)

print(new_lst)
