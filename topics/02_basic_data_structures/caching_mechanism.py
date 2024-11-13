# a function square(n) that calculates the square of an input number n.

calculated_square = {}

def square(n):
    if not n in calculated_square: calculated_square[n] = int(n) ** 2
    return calculated_square[n]
# test cases
# 10 -> 100 -> {'10': 100}
# 5 -> 25 -> {'10': 100, '5': 25}
# 5 -> 25 -> {'10': 100, '5': 25}
print(square("10"))
print(calculated_square)
print(square("5"))
print(calculated_square)
print(square("5"))
print(calculated_square)
