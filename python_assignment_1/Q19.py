input_string = input("Enter a string: ")

if len(input_string) < 2:
    result = ""
else:
    first_two = input_string[:2]
    last_two = input_string[-2:]
    result = first_two + last_two

print("Result:", result)
