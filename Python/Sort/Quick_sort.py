def quickSort(nums):
    quickSortRecursive(nums, 0, nums.length - 1)
    
def quickSortRecursive(nums, left, right):
    if left >= right:
        return;
    pivotPos = partition(nums, left, right)
    
    quickSortRecursive(nums, left, pivotPos - 1)
    quickSortRecursive(nums, pivotPos + 1, right)

def partition(nums, left, right):
    for i in range(left, right):
        if nums[i] < nums[right]:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
    if nums[left] > nums[right]:
        nums[left], nums[right] = nums[right], nums[left]
    return left

nums = {2, 5, 3, 1, 6, 4, 9, 8, 7}
print(nums)
