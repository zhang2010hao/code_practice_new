
def maxProduct(nums):
    n = len(nums)
    mins = [1] * (n+1)
    maxs = [1] * (n+1)

    rest = -11
    for i in range(n):
        min_v = min(mins[i] * nums[i], maxs[i] * nums[i], nums[i])
        max_v = max(mins[i] * nums[i], maxs[i] * nums[i], nums[i])
        mins[i+1] = min_v
        maxs[i+1] = max_v
        rest = max(rest, max_v)

    return rest

nums = [2,3,-2,4]
print(maxProduct(nums))

