import re

# Count a number of Upper case letters in the string.
# E.g. '7865serS3' - 'Number of Capital letters: 1'

regex_one = "[A-Z]"
string_one = "7865serS3"
string_two = "7865sers3"
string_three = "78S65serU3"

def count_capital_in_string(regex_string, test_string):
    pattern = re.compile(regex_string)
    result = re.findall(pattern, test_string)
    return len(result)


def main():
    print(count_capital_in_string(regex_one, string_one))
    print(count_capital_in_string(regex_one, string_two))
    assert count_capital_in_string(regex_one, string_one) == 1
    assert count_capital_in_string(regex_one, string_two) == 0
    assert count_capital_in_string(regex_one, string_three) == 2


if __name__ == "__main__":
    main()
