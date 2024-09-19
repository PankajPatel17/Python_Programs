# How will you compare two lists?

# In python we can compare lists with different methods depending on what aspects of the we want to compare.


#both are equal or not

lst1 = [1,2,5,7,4]
lst2 = [2,3,4,5,6]

if len(lst1) == len(lst2):
    print("both list are equal")
else:
    print("both list are not equal")

#both have same unique element or not

set1 = set(lst1)
set2 = set(lst2)

if set1 == set2:
    print("both have same unique element")
else:
    print("both have different unique element")
