d={101:"pankaj",102:"vaibhav",103:"manoj",104:"sourav"}

print(d)
print(d.get(103))
print(d.items())
print(d.values())
print(d.pop(102))
print(d)
print(d.popitem())
d1={201:"sahil",202:"shubham",203:"sunjay"}
d.update(d1)
print(d)

for i in d:
    print(i, ":", d[i])
d[101]="vikas"
print(d)