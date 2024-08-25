num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

sum = 0

if num1 != num2 and num1 != num3:
    if num2 != num3:
        sum = num1 + num2 + num3
else:
    print("two number are equal so sum is :")
print(sum)