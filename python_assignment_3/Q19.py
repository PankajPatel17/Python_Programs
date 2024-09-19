# How Do You Handle Exceptions With Try/Except/Finally In Python?Explain with coding snippets. 

try:
    x=int(input("Enter Number:"))
    if x%2!=0:
        print("Success Fully!")
    else:
        print("Even Number")
except:
    print("Please enter a valid number")
finally:
    print("Thank you")