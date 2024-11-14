def bubble_sort_asc(arr_asc):
    n = len(arr_asc)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if arr_asc[j] > arr_asc[j+1]:
                arr_asc[j], arr_asc[j+1] = arr_asc[j+1], arr_asc[j]
    return arr_asc

arr_asc = [44, 55, 12, 42, 94, 18, 6, 67]


def bubble_sort_desc(arr_desc):
    n = len(arr_desc)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if arr_desc[j] < arr_desc[j+1]:
                arr_desc[j], arr_desc[j+1] = arr_desc[j+1], arr_desc[j]
    return arr_desc

arr_desc = [44, 55, 12, 42, 94, 18, 6, 67]


def bubble_sort_early_stop(arr_stop):
    n = len(arr_stop)
    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            if arr_stop[j] > arr_stop[j+1]:
                arr_stop[j], arr_stop[j+1] = arr_stop[j+1], arr_stop[j]
                swapped = True

        if not swapped:
            break
    return arr_stop

arr_stop = [6, 12, 18, 42, 94, 55, 44, 67]


print("Ascending Order:", bubble_sort_asc(arr_asc))
print("Descending Order:", bubble_sort_desc(arr_desc))
print("Ascending Order with Early Stopping:", bubble_sort_early_stop(arr_stop))






