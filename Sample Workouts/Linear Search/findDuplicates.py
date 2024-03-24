

def findDuplicates(nums: list[int]) -> list[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                result.append(nums[i])
    return result


reslt = findDuplicates([1, 2, 3, 4, 4, 5, 6, 6, 7])
print(reslt)