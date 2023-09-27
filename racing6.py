
def rearrange_string(input_string):

    upper_letters = []
    lower_letters = []
    
    for char in input_string:
        if char.isupper():
            upper_letters.append(char)
        else:
            lower_letters.append(char)

    upper_letters.sort(reverse=True)
    lower_letters.sort(reverse=True)

    result = ''.join(lower_letters + upper_letters)
    
    return result

input_string = input("Enter a string: ")

output_string = rearrange_string(input_string)
print(output_string)
