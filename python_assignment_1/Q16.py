str = input("Enter a string: ")

poor_index = str.find('poor')

if poor_index != -1:
    not_index = str.find('not', poor_index)

    if not_index != -1:
        result = str[:not_index] + 'good' + str[poor_index + len('poor'):]
    else:
        result = str
else:
    result = str

print(result)
