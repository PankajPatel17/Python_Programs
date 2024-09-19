# Write a Python function that takes two lists and returns true if they have at least one common member.

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]


set1 = set(list1)
set2 = set(list2)

if not set1.isdisjoint(set2):
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")
