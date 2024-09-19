# Write a Python program to remove an empty tuple(s) from a list of tuples.
tpl_lst = [(1,2,3),(7,),(),(4,5,6),()]

new_lst = []

for i in tpl_lst:
    if i:
        new_lst.append(i)

print(new_lst)