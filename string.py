str = input('Enter a string: ')

up = 0
lw = 0
sp = 0
al= 0
num = 0


for i in str:
    if i.isupper():
        up += 1
    elif i.islower():
        lw += 1
    if i.isalpha():
        al += 1
    elif i.isnumeric():
        num += 1
    elif i.isspace():
        sp += 1

print('Upper:', up)
print('Lower:', lw)
print('Number:', num)
print('Space:', sp)
print('Alphabet:', al)


