def remove_duplicate_lines(some_file):
    # Open the file in read mode
    with open(some_file, 'r') as file:
        lines = file.readlines()

    # Remove duplicate lines by converting the list to a set and back to a list
    unique_lines = list(set(lines))

    new_file= 'new_file.txt'
    with open(new_file, 'w') as file:
        file.writelines(unique_lines)

remove_duplicate_lines('file_task1.txt')