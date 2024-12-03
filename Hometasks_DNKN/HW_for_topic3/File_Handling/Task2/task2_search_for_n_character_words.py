import re
def print_n_character_words(some_file, n):
    with open(some_file, 'r') as file:
     text = file.read()
     words = re.findall(r'\b\w+\b', text)
     # words = some_file.split()

    for word in words:
        if len(word) == n:
            print(word)

while True:
    answer = input("lets test the code? (y/n): ")
    if answer == 'y':
        n = int(input("input n: "))
        print_n_character_words('file_task2.txt', n)
    else:
        print(f"D'oh, you've stopped the check!")
        break

