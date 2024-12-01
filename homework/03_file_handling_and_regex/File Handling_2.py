def print_n_character_words(file_path, n):
    # Open and read the file
    with open(file_path, 'r') as file:
        words = file.read().split()

    # Filter words that have exactly 'n' characters
    n_char_words = [word for word in words if len(word) == n]

    # Print filtered words
    for word in n_char_words:
        print(word)


# Define list of lines to write to a file for demonstration
lines_to_write = [
    "Hello, world!\n",
    "This is a test line.\n",
    "Enjoy working with Python.\n",
    "Hello, Python coders!\n"
]

# Create the file with example lines
file_path = "file_handling/example_text.txt"
with open(file_path, 'w') as file:
    file.writelines(lines_to_write)

# Example usage: Print all words with 5 characters
print_n_character_words(file_path, 5)