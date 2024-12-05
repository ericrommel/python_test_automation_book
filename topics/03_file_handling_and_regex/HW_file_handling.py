#Read the file and remove equal lines (if any).
def unique_file_lines(path = ""):
    file = open(path, "r")

    lines = []

    for line in file:
        lines.append(line.rstrip())

    file.close()

    unique_lines = list(set(lines))

    return unique_lines


#test
file_path = r"C:\Users\Veronika_Kravchenko\Documents\Phyton\Python_course\python_test_automation_book\topics\03_file_handling_and_regex\file1.txt"
unique_words = unique_file_lines(file_path)
print(unique_words)


#Print out all words with length of n-characters
def words_length_more_than(n, list):
    #file = open(path, "r")

    words = []

    for word in list:
        if len(word.rstrip()) == n:
            words.append(word.rstrip())

    return words

five_character_words = words_length_more_than(5, unique_words)
print(five_character_words)

#Combine two files into a third file
file_path = r"C:\Users\Veronika_Kravchenko\Documents\Phyton\Python_course\python_test_automation_book\topics\03_file_handling_and_regex\assets\file1.txt"
file_path2 = r"C:\Users\Veronika_Kravchenko\Documents\Phyton\Python_course\python_test_automation_book\topics\03_file_handling_and_regex\assets\file2.txt"
file_path3 = r"C:\Users\Veronika_Kravchenko\Documents\Phyton\Python_course\python_test_automation_book\topics\03_file_handling_and_regex\assets\file4.txt"

def create_third_file(files, new_path):
    new_file = open(new_path, "+w")
    for file_path in files:
        file = open(file_path, "r")

        for line in file:
            new_file.write(line)
        file.close()
    new_file.close()

file_pathes = [file_path, file_path2]
create_third_file(file_pathes, file_path3)

file = open(file_path3, "r")
print(file.read())
file.close()