

def findPeakElement(nums):
    nums.insert(0, float('-inf'))
    nums.append(float('-inf'))
    n = len(nums) - 2

    left = 1
    right = n + 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            ans = mid
            break
        elif nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return ans
