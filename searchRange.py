def searchRange(nums, target):
    def binarysearch(nums, target, isleft):
        left = 0
        right = len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (nums[mid] == target and isleft):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans

    left = binarysearch(nums, target, True)
    right = binarysearch(nums, target, False) - 1

    if left <= right and right < len(nums) and nums[left] == target and nums[right] == target:
        return [left, right]
    else:
        return [-1, -1]


nums = [5, 7, 7, 8, 8]
target = 8
print(searchRange(nums, target))
