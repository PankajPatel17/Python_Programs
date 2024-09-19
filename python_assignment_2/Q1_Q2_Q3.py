#Q1. :- what is list?
#
# a list is a ordered and mutable collection of data. List stores different types of datatypes like integer , string  , foat , boolean etc.
# we can also modify, add,remove or delete this data. List are created with square brackets "[]".

# Example =
# lst = ['1','1.1','helloo','True']

#Q2. :- How will you remove last object from a list?

#ans :- we can remove last object from a list by using 'pop()' method.

# Example :-
# lst = [2, 33, 222, 14, 25]
# lst.pop()
# print(lst)
# 'pop()' method will remove the last element from the list.

#Q3. :- Differentiate between append() and extend() methods?

#ans :- append()-- this method add a single element to the end of the list.
#       extend()-- this method add elements to the end of the list by iterating over another list,tuple or dictionary.

#Example :- append()--
            # lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            # lst.append('10')
            # print(lst)

            #extend()--
            # lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            # lst1 = ['A', 'B', 'C', 'D']
            # lst.extend(lst1)
            # print(lst)