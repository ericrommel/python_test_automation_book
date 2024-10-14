import re

# Define if a string contains the required characters.
# E.g. if '7865serS3' includes '583' - True; '973' - False

regex_one = "583"
regex_two = "973"
string_one = "7865serS3"


def all_chars_are_in_string(regex_string, test_string):
    for x in regex_string:
        # if re.search(re.escape(x), test_string):
        if re.search(re.compile(x), test_string):
            continue
        else:
            return False
    return True

    # return all(re.search(re.escape(char), test_string) for char in regex_string)


def main():
    print(all_chars_are_in_string(regex_one, string_one))
    print(all_chars_are_in_string(regex_two, string_one))
    print(all_chars_are_in_string("res", string_one))
    print(all_chars_are_in_string("rest", string_one))


if __name__ == "__main__":
    main()
