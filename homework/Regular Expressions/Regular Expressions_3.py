import re
def contains_upper_followed_by_lower(input_string):

    # Regular expression to find uppercase followed by lowercase letters
    pattern = re.compile(r'[A-Z][a-z]+')
    # Search for the pattern in the string
    match = pattern.search(input_string)
    # Return True or False if the pattern is found/not found
    return bool(match)

example_1 = "75serS3"
example_2 = "75WseTrS3"

result1 = contains_upper_followed_by_lower(example_1)
result2 = contains_upper_followed_by_lower(example_2)

print(f"'{example_1}' contains an uppercase letter followed by lowercase letters: {result1}")
print(f"'{example_2}' contains an uppercase letter followed by lowercase letters: {result2}")