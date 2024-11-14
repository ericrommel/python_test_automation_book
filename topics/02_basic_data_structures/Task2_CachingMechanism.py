cache = {}

def square(n):
    result = float(n) * float(n)
    cache[n] = result
    return result


def check_cache(n):
    if n in cache:
        return float(cache[n])
    else:
        return ()

def return_result(n):
    x = check_cache(n)
    if x == ():
        return square(n)
    else:
        print(f"Returning cached value for: {n}")
        return x

numbers = [8, 6, 2, 8, 2, -3]

for i in numbers:
    print(return_result(i))
    print("------")


