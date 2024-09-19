lst = ["Pankaj","Vaibhav","Manoj","sourav"]

max_len = 0

for i in lst:
    if len(i) > max_len:
        max_len = len(i)
print("the len. of longest word is : ",max_len)