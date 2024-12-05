# Define if a string contains the required characters. E.g. if '7865serS3' includes '583' - True; '973' - False
import re

def contains_chars(main_string, required_string):

    pattern = ''.join([f'(?=.*{char})' for char in required_string])

    # Search the main_string using the pattern
    if re.search(pattern, main_string):
        return True
    else:
        return False

# test
print(contains_chars('7865serS3', '583'))  # -> True
print(contains_chars('7865serS3', '973'))  # -> False

#Count a number of Upper case letters in the string. E.g. '7865serS3' - 'Number of Capital letters: 1'
import re

def count_letters(input_string):
    uppercase_letters = re.findall(r'[A-Z]', input_string)

    return len(uppercase_letters)

# test
input_string = '7865serS3'
print(count_letters(input_string)) # ->1

#Define if the string contains at least one Upper case letter followed by Lower case letters. E.g. '75serS3' - False; '75WseTrS3' - True;
import re

def contains_upper_letters(input_string):

    if re.search(r'[A-Z][a-z]', input_string):
        return True
    else:
        return False
# test
print(contains_upper_letters('75serS3'))  # ->False
print(contains_upper_letters('75WseTrS3'))  # ->True

