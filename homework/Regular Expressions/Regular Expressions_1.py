import re
def contains_required_characters(input_string, required_chars):

    pattern = ''.join(f'(?=.*{re.escape(char)})' for char in required_chars)

    # Compile the regex pattern
    regex = re.compile(pattern)

    # Search the pattern in the input string
    return bool(regex.search(input_string))

required_chars = "583"
input_string_with_required_chars = "7865serS3"
input_string_without_required_chars = "786serS3"

result1 = contains_required_characters(input_string_with_required_chars, required_chars)
result2 = contains_required_characters(input_string_without_required_chars, required_chars)

print(f"String '{input_string_with_required_chars}' contains all characters '{required_chars}': {result1}")
print(f"String '{input_string_without_required_chars}' contains all characters '{required_chars}': {result2}")