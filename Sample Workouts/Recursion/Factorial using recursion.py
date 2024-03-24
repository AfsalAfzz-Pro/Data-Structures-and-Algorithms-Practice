
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


num = 6
result = factorial(num)
print(result)
