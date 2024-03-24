

def findReverse(n):
    if len(n) <= 1:
        return n
    return findReverse(n[1:]) + n[0]


result = findReverse("hello world")
print(result)


