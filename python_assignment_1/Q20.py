str1 = input("Enter the first string: ")
str2 = input("Enter the string to insert: ")

str3 = len(str1) // 2

str4 = str1[:str3] + str2 + str1[str3:]

print("Result:", str4)
