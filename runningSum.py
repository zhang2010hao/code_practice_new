
def runningSum(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        nums[i] = s

    return nums

nums = [1, 2, 3, 4]
rst = runningSum(nums)
print(rst)