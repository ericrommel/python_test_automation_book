import re
def count_uppercase_letters(input_string):

    # Regular expression to find uppercase letters
    uppercase_letters = re.findall(r'[A-Z]', input_string)
    return len(uppercase_letters)

input_string = "78AAa65serS3"
uppercase_count = count_uppercase_letters(input_string)
print(f"Number of Capital letters: {uppercase_count}")