
# factorial program using recursion
def factorial(n):
    value = 1
    if n <= 1:
        print("n", n)
        return n
    print(n)
    return n * factorial(n-1)
    
    # return n * factorial(n-1)


result = factorial(5)
print(result)
