# Write a function to replace each alphabet in the given string with
# another alphabet occurring at the n-th position from each of them.

def replaceString(strs: str, k: int):
    string = list(strs)
    try:
        for i in range(len(strs)):
            new = i + k
            string[i] = string[new]
            # print(string)
    except IndexError:
        return ''.join(string)


result = replaceString("afsal", 2)
print(result)


