

def checkElem(nums: list[int], target: int):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        mid_value = nums[mid]
        print(mid)
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


numbers = [1, 2, 3, 4, 5, 6, 7]
targett = 1
result = checkElem(numbers, targett)
print(f"{targett} is present at index {result}")