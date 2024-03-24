def find_target(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums)
    mid = (start + end)//2
    while start < end:
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid + 1
        if nums[mid] > target:
            end = mid - 1
        mid = (start + end)//2


result = find_target([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13)
print(result)
