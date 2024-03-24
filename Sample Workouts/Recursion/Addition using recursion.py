

def findSum(n):
    if n == 1:
        return 1
    return n + findSum(n-1)


num = 4
result = findSum(num)
print(result)