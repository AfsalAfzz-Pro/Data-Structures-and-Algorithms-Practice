

def countOccurrences(nums: list[int], value: int) -> int:
    count = 0
    for num in nums:
        if num == value:
            count += 1

    return count


result = countOccurrences([1, 2, 2, 3, 4, 5, 2], 2)
print(result)

