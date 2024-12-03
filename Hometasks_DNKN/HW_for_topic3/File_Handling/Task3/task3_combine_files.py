def combine_files(file1, file2, output_file):

    with open(file1, 'r') as file1:
        content1 = file1.read()


    with open(file2, 'r') as file2:
        content2 = file2.read()

    combine_content = content1 + "\n" + content2

    with open(output_file, 'w') as output_file:
        output_file.write(combine_content)


output_file = 'combined_file.txt'
combine_files('file1.txt', 'file2.txt', 'combined_file.txt')