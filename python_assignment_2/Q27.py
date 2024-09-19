# Write a Python program to find the repeated items of a tuple.

my_tpl = (1,2,3,33,32,2,4,4,33)



unique_items = set()
repeated_items = set()

for item in my_tpl:
    if item in unique_items:
        repeated_items.add(item)
    else:
        unique_items.add(item)

print("Original tuple:", my_tpl)
print("Repeated items:", list(repeated_items))
