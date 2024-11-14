'''
Research about `Caching Mechanism` and then, implement a caching mechanism for a function that calculates the square of a number. Instructions:    
- Define a function `square(n)` that calculates the square of an input number n.    
- Implement a cache using a dictionary to store previously computed squares.    
- Modify the `square(n)` function to check if the result for the given n is already in the cache:    
- If it is, return the cached result.    
- If it is not, compute the square, store it in the cache, and then return the result.  
'''  

# Initialize the cache as a dictionary
cache = {}

def square(n):
    # Check if the result is already in the cache
    if n in cache:
        print(f"Returning cached result for {n}")
        return cache[n]
    
    # If not in cache, compute the square
    result = n * n
    # Store the result in the cache
    cache[n] = result
    print(f"Computed and cached result for {n}")
    return result

print(square(5))
print(square(5))
print(square(2))
print(square(2))