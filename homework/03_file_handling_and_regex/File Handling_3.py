def create_file(file_path, content):
    #Create a file with the given content
    with open(file_path, 'w') as file:
        file.writelines(content)

def combine_files(file1_path, file2_path, combined_file_path):
    #Combine two files into a third file.
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.readlines()
        content2 = file2.readlines()

    with open(combined_file_path, 'w') as combined_file:
        combined_file.writelines(content1)
        combined_file.writelines(content2)

# Create files
content_file1 = ["First line of file 1\n", "Second line of file 1\n"]
file1_path = "file_handling/file1.txt"
create_file(file1_path, content_file1)

content_file2 = ["First line of file 2\n", "Second line of file 2\n"]
file2_path = "file_handling/file2.txt"
create_file(file2_path, content_file2)

# Combine files into a third file
combined_file_path = "file_handling/combined_file.txt"
combine_files(file1_path, file2_path, combined_file_path)
print(f"Successfully combined {file1_path} and {file2_path} into {combined_file_path}")