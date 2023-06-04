def minimumMountainRemovals(nums):
    up_dp = []
    for i in range(len(nums)):
        up_dp.append(1)
        for j in range(i):
            if nums[i] > nums[j]:
                up_dp[i] = max(up_dp[i], up_dp[j] + 1)

    down_dp = []
    for i in range(len(nums) - 1, -1, -1):
        down_dp.append(1)
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                down_dp[-1] = max(down_dp[-1], down_dp[len(nums) - 1 - j] + 1)

    max_len = 0
    for i in range(1, len(nums) - 1):
        v1 = up_dp[i]
        v2 = down_dp[len(nums) - 1 - i]
        if v1 > 1 and v2 > 1:
            max_len = max(max_len, v1 + v2)

    return len(nums) - max_len + 1



nums = [100,92,89,77,74,66,64,66,64]
rest = minimumMountainRemovals(nums)
print(rest)
