'''
Research about Caching Mechanism and then, implement a caching mechanism for a function that calculates the square of a number. Instructions:
Define a function square(n) that calculates the square of an input number n.
Implement a cache using a dictionary to store previously computed squares.
Modify the square(n) function to check if the result for the given n is already in the cache:
If it is, return the cached result.
If it is not, compute the square, store it in the cache, and then return the result.y
'''
cache = {}

def square(n):
    if n in cache:
        print(f"Fetching from cache for {n}")
        return cache[n]
    else:
        result = n * n
        cache[n] = result
        print(f"Computing and caching for {n}")
        return result


while True:
    answer = input("lets test the code? (y/n): ")
    if answer == 'y':
        n = int(input("input n: "))
        print(square(n))
    else:
        print(f"doh, you've stopped the calculation")
        break

print(f"results in cache: {cache}")

