# Bubble Sort Algorithm

#  Bubble sorting in ascending order regular one
bubble = [3, 5 ,6, 9, 8, 7, 1, 2]
sorted = False

for i in range(0, len(bubble)):
    for i in range (0, len(bubble) - 1):
        if bubble[i] > bubble[i + 1]:
            nex_el = bubble[i + 1]
            bubble[i + 1] = bubble[i]
            bubble[i] = nex_el
            sorted = True

    sorted = not(sorted)

print(bubble)
print("end")

# Bubble sorting with early stopping

bubble = [3, 5 ,6, 9, 8, 7, 1, 2]
sorted = False

while sorted == False:
    for i in range (0, len(bubble) - 1):
        if bubble[i] > bubble[i + 1]:
            nex_el = bubble[i + 1]
            bubble[i + 1] = bubble[i]
            bubble[i] = nex_el
            sorted = True

    sorted = not(sorted)

print(bubble)
print("end")

# Bubble sorting in descending order

bubble = [3, 5 ,6, 9, 8, 7, 1, 2]
sorted = False

while sorted == False:
    for i in range (0, len(bubble) - 1):
        if bubble[i] < bubble[i + 1]:
            nex_el = bubble[i + 1]
            bubble[i + 1] = bubble[i]
            bubble[i] = nex_el
            sorted = True

    sorted = not(sorted)

print(bubble)