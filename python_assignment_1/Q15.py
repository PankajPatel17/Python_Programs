str = input("Enter a string: ")

len = len(str)

if len < 3:
    result = str
elif str.endswith("ing"):
    result = str + "ly"
else:
    result = str + "ing"

print(result)
