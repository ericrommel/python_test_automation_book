cache = {}
def square(n):
     if n in cache:
         print(f'{cache[n]} cached')
         return cache[n]

     result = (n ** 2)
     cache[n] = result
     print(f'{cache[n]} culculated')
     return result


my_list = [2, 2, 3, 3, 4]
squared_list = [square(num) for num in my_list]
print(squared_list)

