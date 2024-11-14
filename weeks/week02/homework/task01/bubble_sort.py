#Ascending Order: Sorts by always moving larger elements to the end
test_list = [10, 1, 2, 3, 8, 5, 6, 7, 11, -2]

def swap (arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    

def bubble_sort_ascending(arr):
    for itm in arr:
        for idx in range(len(arr) - 1):
            if arr[idx] > arr [idx +1]:
                swap (arr, idx, idx + 1)
    return arr 

print("Sorted list in ASC order:" , bubble_sort_ascending(test_list))

#Descending Order: Sorts by always moving smaller elements to the end  

def bubble_sort_descending(arr):
    n = len(arr)
    for idx in range(n - 1):
            if arr[idx] < arr [idx +1]:
                swap (arr, idx, idx + 1)
    return arr 

print("Sorted list in DESC order:" , bubble_sort_descending(test_list))

#Early Stopping: Improves efficiency by halting if no swaps are made during a pass, meaning the list is already sorted

def bubble_sort_descending_with_early_stopping(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for idx in range(n - 1 - i):
            if arr[idx] < arr [idx +1]:
                swap (arr, idx, idx + 1)
                swapped = True
        if not swapped: 
            break
    return arr 

print("Sorted list in DESC order with early stop:" , bubble_sort_descending_with_early_stopping(test_list))    