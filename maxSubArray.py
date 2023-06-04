def maxSubArray(nums):
    dp = [nums[0]]

    for i in range(1, len(nums)):
        tmp = max(dp[i - 1] + nums[i], nums[i])
        dp.append(tmp)

    max_sum = max(dp)

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
