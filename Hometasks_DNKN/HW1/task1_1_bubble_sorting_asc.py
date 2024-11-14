'''
Research about the Bubble Sort Algorithm in Python. Implement three version of it:
In ascending order (regular one)
'''
import random

def bubble_sort_ascending(random_numbers):
    n = len(random_numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if random_numbers[j] > random_numbers[j+1]:
                random_numbers[j], random_numbers[j+1] = random_numbers[j+1], random_numbers[j]
                swapped = True
        # if not swapped:
        #     break
    return random_numbers


random_numbers = [random.randint(0, 100) for k in range(20)]
print(f'a list of 20 random numbers from 0 to 20: {random_numbers}')

print(f'random numbers sorted in ascending order: {bubble_sort_ascending(random_numbers)}')