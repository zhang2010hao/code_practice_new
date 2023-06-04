def maxValueAfterReverse(nums):
    # https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/solutions/1704860/by-yuigahama-tsn5/
    n = len(nums)

    s = 0
    for i in range(n - 1):
        s += abs(nums[i + 1] - nums[i])

    maxL = min(nums[0], nums[1])
    minR = max(nums[0], nums[1])
    for i in range(n):
        if i < n-1:
            maxL = max(maxL, min(nums[i], nums[i + 1]))

        if i > 0:
            minR = min(minR, max(nums[i-1], nums[i]))

    if maxL > minR:
        rst = s + 2 * (maxL - minR)
    else:
        rst = s

    for i in range(n - 1):
        rst = max(rst, s - abs(nums[i+1] - nums[i]) + abs(nums[0] - nums[i+1]),
                  s - abs(nums[i+1] - nums[i]) + abs(nums[n-1] - nums[i]))

    return rst

nums = [2,5,1,3,4]
rest = maxValueAfterReverse(nums)
print(rest)
