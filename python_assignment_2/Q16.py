#Write a Python program to check whether a list contains a sub list

main_list = [11,22,32,43,12,32]
sub_list = [32,43,12]

main_str = str(main_list)
sub_str = str(sub_list)

found = sub_str in main_str

if found:
    print("list contains a sub list")
else:
    print("list does not contain a sub list")
