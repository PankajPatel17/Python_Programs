def checkvalues(num1,num2):
    # num1 = int(input("Enter a number: "))
    # num2 = int(input("Enter another number: "))

    if num1 == num2:
        return True
    elif num1 + num2 == 5:
        return True
    elif abs(num1 - num2)==5 :
        return True
    else:
        return False

print(checkvalues(5,6))
