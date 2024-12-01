def create_file_with_duplicates(file_path, lines):
    # Write potentially duplicated lines to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

    # Reading the file to remove duplicates
    unique_lines = set()
    with open(file_path, 'r') as file:
        for line in file:
            unique_lines.add(line)

    # Write the unique lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(unique_lines)


#  list of lines including  duplicates
lines_to_write = [
    "Hello, world!\n",
    "This is a test line.\n",
    "This is a test line.\n",
    "Python is great.\n",
    "Hello, world!\n"  
]

file_path = "file_handling/example_with_duplicates.txt"
create_file_with_duplicates(file_path, lines_to_write)