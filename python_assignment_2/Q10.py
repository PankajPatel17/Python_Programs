#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

lst = []

for i in range(1,31):
    i = i**2
    lst.append(i)

first_five_elements = lst[:5]
last_five_elements = lst[-5:]

print("first five elements: ", first_five_elements)
print("last five elements: ", last_five_elements)


