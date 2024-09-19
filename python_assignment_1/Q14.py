str1 = input("Enter a string: ")
str2 = input("Enter another string: ")


if len(str1) >= 2:
    str1 = str1[1] + str1[0] + str1[2:]
if len(str2) >= 2:
    str2 = str2[1] + str2[0] + str2[2:]

result = str1 + " " + str2

print(result)