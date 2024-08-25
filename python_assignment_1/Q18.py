str = "helo"

len = len(str)
result = 0

if len%4==0 :
    result = str[::-1]
else:
    result = str

print(result)
