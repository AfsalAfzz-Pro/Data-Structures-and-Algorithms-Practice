
# This is a program to find sum using recursion
def add(num):
    if num <= 0:
        return num
    return num + add(num-1)


result = add(5)
print(result)
